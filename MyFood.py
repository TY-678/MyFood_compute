from PyQt5 import QtCore, QtGui, QtWidgets
from user_info import FoodComputer
from maingui import Ui_MainWindow
from PIL import Image
from ultralytics import YOLO
import cv2
from io import BytesIO
import numpy as np

# import mysql.connector
from datetime import datetime

# from myfood_sql import *
from PyQt5.QtWidgets import QApplication, QMessageBox
import ast

from myfood_compute.api.schema.user_schema import UserInfo, UserFoodHistory
from myfood_compute.api.schema.food_schema import ProductInfo
import requests
import handle_requests


class MyApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()

        # 創建 GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 連接按鈕點擊事件
        self.ui.update_userinfo_Button.clicked.connect(self.update_user_info)
        self.ui.take_photo_Button.clicked.connect(self.take_photo)
        self.ui.save_Button.clicked.connect(self.save_toady_food)
        self.ui.add_to_list_Button.clicked.connect(self.add_to_database)
        self.ui.date_Button.clicked.connect(self.check_list)
        self.ui.delete_list_Button.clicked.connect(self.delete_list)

        # 初始化攝影機
        self.capture = cv2.VideoCapture(0)

        # # 設定影像尺寸
        # width = 128  # 設定寬度
        # height = 96  # 設定高度
        # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 更新畫面的頻率，單位是毫秒

        # 初始化 YOLO 模型
        self.yolo = YOLO("weight/best_1115.pt")

        # scan list
        self.scan_list = []

        # TODO -> change sql
        # connect sql
        # self.sql = DatabaseConnector()

        # # 資料庫讀取主頁的五個欄位
        # self.sql.sql_connect()
        # self.sql.cursor.execute(f"SELECT * FROM user_info ORDER BY id DESC LIMIT 1;")
        # user_info = self.sql.cursor.fetchall()
        # self.sql.sql_close()
        user_info = handle_requests.get_user_info()

        # user_height = float(user_info[0][1])
        # user_weight = float(user_info[0][2])
        # target_weight = float(user_info[0][3])
        # target_time = float(user_info[0][4])
        # tdee = float(user_info[0][5])
        self.user_info = FoodComputer(
            user_height=user_info.height,
            user_weight=user_info.weight,
            target_weight=user_info.target_weight,
            target_time=user_info.target_time,
            tdee=user_info.tdee,
        )

        self.ui.now_weight.setPlainText(str(f"{user_info[0][2]:.1f}"))
        self.ui.days.setPlainText(str(f"{user_info[0][4]:.0f}"))
        self.user_info.can_eat = self.user_info.count_cal_day()
        self.ui.can_eat.setPlainText(str(f"{self.user_info.can_eat:.1f}"))
        self.ui.day_total.setPlainText(str(f"{self.user_info.day_total:.1f}"))
        self.ui.pred_weight.setPlainText(str(f"{self.user_info.pred_weight():.1f}"))

    def update_user_info(self):
        # 獲取使用者輸入的數值
        (
            self.user_info.user_height,
            self.user_info.user_weight,
            self.user_info.target_weight,
            self.user_info.target_time,
            self.user_info.tdee,
        ) = self.ui.update_userinfo()

        # TODO -> update sql
        # user info save to database
        # self.sql.sql_connect()
        # self.sql.cursor.execute(
        #     f"""insert into user_info
        #     (height, weight, target_weight, target_time, tdee)
        #     values ({self.user_info.user_height}, {self.user_info.user_weight}, {self.user_info.target_weight}, {self.user_info.target_time}, {self.user_info.tdee});"""
        # )
        # self.sql.sql_close()
        new_user_info = UserInfo(
            height=self.user_info.user_height,
            weight=self.user_info.user_weight,
            target_weight=self.user_info.target_weight,
            target_time=self.user_info.target_time,
            tdee=self.user_info.tdee,
        )
        handle_requests.update_user_info(new_user_info=new_user_info)

        # 顯示在主頁的五個欄位中
        self.ui.now_weight.setPlainText(str(f"{self.user_info.user_weight:.1f}"))
        self.ui.days.setPlainText(str(f"{self.user_info.target_time:.0f}"))
        self.user_info.can_eat = self.user_info.count_cal_day()
        self.ui.can_eat.setPlainText(str(f"{self.user_info.can_eat:.1f}"))
        self.ui.day_total.setPlainText(str(f"{self.user_info.day_total:.1f}"))
        self.ui.pred_weight.setPlainText(str(f"{self.user_info.pred_weight():.1f}"))

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(
                frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888
            )
            pixmap = QtGui.QPixmap.fromImage(image)
            if not self.ui.graphicsView.scene():
                self.ui.graphicsView.setScene(QtWidgets.QGraphicsScene())
            self.ui.graphicsView.scene().clear()
            self.ui.graphicsView.scene().addPixmap(pixmap)

    def take_photo(self):
        ret, frame = self.capture.read()
        if ret:
            # 將拍攝的照片轉換成 PIL Image
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Ngrok url
            # ngrok_url = url
            img_bytesio = BytesIO()
            pil_image.save(img_bytesio, format="JPEG")
            img_bytes = img_bytesio.getvalue()
            files = {"file": ("image.jpg", img_bytes, "image/jpeg")}
            # response = requests.post(f"{ngrok_url}/image/upload", files=files)
            result_list = handle_requests.upload_image(file=files)
            # TODO

            # float_list = ast.literal_eval(resultslist)

            # self.scan_list = [int(num) for num in float_list]
            self.scan_list = [int(num) for num in result_list]

            # 將 food_list 顯示在 listWidget 中
            self.ui.listWidget.clear()
            print_list = ["Name", "Cal", "Pro"]
            self.ui.listWidget.addItem(
                f"{print_list[0]:<13}{print_list[1]:>10}{print_list[2]:>10}"
            )
            for food in self.scan_list:
                # TODO -> change sql
                # self.sql.sql_connect()
                # self.sql.cursor.execute(
                #     f"select Product, Calories, Carbohydrate, Protein, Fat, Sodium, Sugar from food_list where ID = '{food}';"
                # )
                # f = self.sql.cursor.fetchall()

                # self.sql.sql_close()
                f = handle_requests.get_food(id=food)
                self.ui.listWidget.addItem(
                    f"{f.product:13}{f.calories:10}{f.protein:10}"
                )
                # for i in f:
                #     self.ui.listWidget.addItem(f"{i[0]:13}{i[1]:10}{i[3]:10}")

    # save to database
    def add_to_database(self):
        # get date
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime(
            "%Y,{:d},{:d}".format(current_datetime.month, current_datetime.day)
        )

        for food in self.scan_list:

            # TODO -> change sql

            # # add to user_food_history
            # self.sql.sql_connect()
            # self.sql.cursor.execute(
            #     f"insert into user_food_history values ('{formatted_date}', {food})"
            # )
            # self.sql.sql_close()
            new_history = UserFoodHistory(food_id=food, date=formatted_date)
            handle_requests.add_user_history(new_history=new_history)

        self.delete_list()

    def save_toady_food(self):
        # 加入彈出視窗顯示結果

        can_eat = float(self.user_info.can_eat)
        day_total = float(self.user_info.day_total)

        def show_message(can_eat, day_total):

            msg_box = QMessageBox()

            message = f"""
            每日建議攝取熱量 : {can_eat:>6.1f} Cal
            本日總共攝取熱量 : {day_total:>6.1f} Cal
            """
            if can_eat > day_total:
                message += f"還可以再吃 : {can_eat - day_total:>6.1f} Cal"
            elif can_eat < day_total:
                message += f"本日攝取熱量超過建議量 : {day_total - can_eat:>6.1f} Cal"
            else:
                message += f"攝取熱量剛好符合建議值"

            msg_box.setWindowTitle("今日統計")
            msg_box.setText(message)
            msg_box.setIcon(QMessageBox.Information)

            msg_box.addButton(QMessageBox.Ok)
            msg_box.exec_()

        show_message(can_eat, day_total)
        self.ui.day_total.setPlainText(str(f"{self.user_info.day_total:.1f}"))
        self.ui.pred_weight.setPlainText(str(f"{self.user_info.pred_weight():.1f}"))

    def delete_list(self):
        self.scan_list = []

    def check_list(self):
        check_date = str(self.ui.dateEdit.date().getDate())
        check_date = check_date.replace(" ", "").replace("(", "").replace(")", "")

        # check date
        self.ui.listWidget_2.clear()

        # TODO -> change sql
        # self.sql.sql_connect()

        # self.sql.cursor.execute(
        #     f"select Product, Calories, Carbohydrate, Protein, Fat, Sodium, Sugar\
        #                         from food_list\
        #                         join user_food_history\
        #                         on food_list.ID = user_food_history.ID\
        #                         where Date = '{check_date}';"
        # )
        # f = self.sql.cursor.fetchall()
        # self.sql.sql_close()
        user_food_history = handle_requests.get_user_history(date=check_date)

        print_line = f"-----------------------------------------------------------"
        Nutrients = ["Cal", "Carb", "Pro", "Fat", "Na", "Sug"]
        self.ui.listWidget_2.addItem(
            f"{check_date:<10} :{Nutrients[0]:>9}{Nutrients[1]:>7}{Nutrients[2]:>7}{Nutrients[3]:>7}{Nutrients[4]:>7}{Nutrients[5]:>8}"
        )
        self.ui.listWidget_2.addItem(f"{print_line}")
        total = [0, 0, 0, 0, 0, 0]
        for food in user_food_history:
            self.ui.listWidget_2.addItem(
                f"{food.product:<15}{food.calories:>7.1f}{food.carbohydrate:>7.1f}{food.protein:>7.1f}{food.fat:>7.1f}{food.sodium:>8.1f}{food.sugar:>7.1f} "
            )
            total[0] += food.calories
            total[1] += food.carbohydrate
            total[2] += food.protein
            total[3] += food.fat
            total[4] += food.sodium
            total[5] += food.sugar
        self.ui.listWidget_2.addItem(f"{print_line}")
        self.ui.listWidget_2.addItem(
            f"Total : {total[0]:>14.1f}{total[1]:>7.1f}{total[2]:>7.1f}{total[3]:>7.1f}{total[4]:>8.1f}{total[5]:>7.1f} \n"
        )
        total = [0, 0, 0, 0, 0, 0]

        # check today
        self.ui.listWidget_3.clear()
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime(
            "%Y,{:d},{:d}".format(current_datetime.month, current_datetime.day)
        )

        # TODO -> change sql
        # self.sql.sql_connect()

        # self.sql.cursor.execute(
        #     f"select Product, Calories, Carbohydrate, Protein, Fat, Sodium, Sugar\
        #                         from food_list\
        #                         join user_food_history\
        #                         on food_list.ID = user_food_history.ID\
        #                         where Date = '{formatted_date}';"
        # )
        # f = self.sql.cursor.fetchall()
        # self.sql.sql_close()
        f = handle_requests.get_user_history(date=formatted_date)

        self.ui.listWidget_3.addItem(
            f"Today :{Nutrients[0]:>14}{Nutrients[1]:>7}{Nutrients[2]:>7}{Nutrients[3]:>7}{Nutrients[4]:>7}{Nutrients[5]:>8}"
        )
        self.ui.listWidget_3.addItem(f"{print_line}")
        total = [0, 0, 0, 0, 0, 0]
        for food in user_food_history:
            self.ui.listWidget_3.addItem(
                f"{food.product:<15}{food.calories:>7.1f}{food.carbohydrate:>7.1f}{food.protein:>7.1f}{food.fat:>7.1f}{food.sodium:>8.1f}{food.sugar:>7.1f} "
            )
            total[0] += food.calories
            total[1] += food.carbohydrate
            total[2] += food.protein
            total[3] += food.fat
            total[4] += food.sodium
            total[5] += food.sugar
            # for j in range(1, 7):
            #     total[j - 1] += float(i[j])
        self.ui.listWidget_3.addItem(f"{print_line}")
        self.ui.listWidget_3.addItem(
            f"Total : {total[0]:>14.1f}{total[1]:>7.1f}{total[2]:>7.1f}{total[3]:>7.1f}{total[4]:>8.1f}{total[5]:>7.1f}\n"
        )
        self.user_info.day_total = total[0]
        self.ui.day_total.setPlainText(str(f"{self.user_info.day_total:.1f}"))
        self.ui.pred_weight.setPlainText(str(f"{self.user_info.pred_weight():.1f}"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    my_app = MyApplication()
    my_app.show()
    sys.exit(app.exec_())
