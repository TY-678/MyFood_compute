from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 601, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(80, 50, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(80, 90, 111, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(80, 190, 281, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(80, 150, 161, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(80, 120, 301, 31))
        self.label_10.setObjectName("label_10")
        self.now_weight = QtWidgets.QTextBrowser(self.tab)
        self.now_weight.setGeometry(QtCore.QRect(370, 40, 131, 31))
        self.now_weight.setObjectName("now_weight")
        self.days = QtWidgets.QTextBrowser(self.tab)
        self.days.setGeometry(QtCore.QRect(370, 80, 131, 31))
        self.days.setObjectName("days")
        self.can_eat = QtWidgets.QTextBrowser(self.tab)
        self.can_eat.setGeometry(QtCore.QRect(370, 120, 131, 31))
        self.can_eat.setObjectName("can_eat")
        self.pred_weight = QtWidgets.QTextBrowser(self.tab)
        self.pred_weight.setGeometry(QtCore.QRect(370, 200, 131, 31))
        self.pred_weight.setObjectName("pred_weight")
        self.day_total = QtWidgets.QTextBrowser(self.tab)
        self.day_total.setGeometry(QtCore.QRect(370, 160, 131, 31))
        self.day_total.setObjectName("day_total")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.take_photo_Button = QtWidgets.QPushButton(self.tab_2)
        self.take_photo_Button.setGeometry(QtCore.QRect(20, 330, 113, 32))
        self.take_photo_Button.setObjectName("take_photo_Button")
        self.add_to_list_Button = QtWidgets.QPushButton(self.tab_2)
        self.add_to_list_Button.setGeometry(QtCore.QRect(310, 330, 113, 32))
        self.add_to_list_Button.setObjectName("add_to_list_Button")
        self.delete_list_Button = QtWidgets.QPushButton(self.tab_2)
        self.delete_list_Button.setGeometry(QtCore.QRect(430, 330, 113, 32))
        self.delete_list_Button.setObjectName("delete_list_Button")

        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 271, 291))
        self.graphicsView.setObjectName("graphicsView")

        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(300, 20, 281, 291))
        self.listWidget.setObjectName("listWidget")
        
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_3)
        self.dateEdit.setGeometry(QtCore.QRect(40, 10, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.date_Button = QtWidgets.QPushButton(self.tab_3)
        self.date_Button.setGeometry(QtCore.QRect(30, 40, 113, 32))
        self.date_Button.setObjectName("date_Button")
        # add button
        self.save_Button = QtWidgets.QPushButton(self.tab_3)
        self.save_Button.setGeometry(QtCore.QRect(30, 75, 113, 32))
        self.save_Button.setObjectName("save_Button")
        
        # self.listView_2 = QtWidgets.QListView(self.tab_3)
        # self.listView_2.setGeometry(QtCore.QRect(160, 10, 421, 351))
        # self.listView_2.setObjectName("listView_2")
        # view -> widget
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 155, 421, 350))
        self.listWidget_2.setObjectName("listWidget_2")

        # add today list
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_3.setGeometry(QtCore.QRect(160, 10, 421, 140))
        self.listWidget_3.setObjectName("listWidget_3")



        
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.user_height = QtWidgets.QTextEdit(self.tab_4)
        self.user_height.setGeometry(QtCore.QRect(290, 50, 111, 31))
        self.user_height.setObjectName("user_height")
        self.target_time = QtWidgets.QTextEdit(self.tab_4)
        self.target_time.setGeometry(QtCore.QRect(290, 170, 111, 31))
        self.target_time.setObjectName("target_time")
        self.target_weight = QtWidgets.QTextEdit(self.tab_4)
        self.target_weight.setGeometry(QtCore.QRect(290, 130, 111, 31))
        self.target_weight.setObjectName("target_weight")
        self.user_weight = QtWidgets.QTextEdit(self.tab_4)
        self.user_weight.setGeometry(QtCore.QRect(290, 90, 111, 31))
        self.user_weight.setObjectName("user_weight")
        self.tdee = QtWidgets.QTextEdit(self.tab_4)
        self.tdee.setGeometry(QtCore.QRect(290, 210, 111, 31))
        self.tdee.setObjectName("tdee")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(180, 60, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(180, 180, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(180, 100, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(180, 220, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(180, 140, 60, 16))
        self.label_5.setObjectName("label_5")
        self.update_userinfo_Button = QtWidgets.QPushButton(self.tab_4)
        self.update_userinfo_Button.setGeometry(QtCore.QRect(290, 260, 113, 32))
        self.update_userinfo_Button.setObjectName("update_userinfo_Button")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 加入文字設定

        self.listWidget_3.setStyleSheet('font-family: "Courier New", monospace;')
        self.listWidget_2.setStyleSheet('font-family: "Courier New", monospace;')
        self.listWidget.setStyleSheet('font-family: "Courier New", monospace;')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Food"))
        self.label_6.setText(_translate("MainWindow", "目前體重"))
        self.label_7.setText(_translate("MainWindow", "目標天數"))
        self.label_8.setText(_translate("MainWindow", "若未來飲食皆與今天相同，目標日體重為"))
        self.label_9.setText(_translate("MainWindow", "目前每日飲食熱量"))
        self.label_10.setText(_translate("MainWindow", "每日攝取多少熱量，在目標日可達成目標體重"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主頁"))
        self.take_photo_Button.setText(_translate("MainWindow", "拍照"))
        self.add_to_list_Button.setText(_translate("MainWindow", "加入"))
        self.delete_list_Button.setText(_translate("MainWindow", "重新拍攝"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "加入食物"))
        self.date_Button.setText(_translate("MainWindow", "查詢"))

        #add
        self.save_Button.setText(_translate("MainWindow", "完成本日飲食"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "飲食紀錄"))
        self.user_height.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cm</p></body></html>"))
        self.target_time.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">days</p></body></html>"))
        self.target_weight.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kg</p></body></html>"))
        self.user_weight.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kg</p></body></html>"))
        self.tdee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kcal</p></body></html>"))
        self.label.setText(_translate("MainWindow", "身高"))
        self.label_2.setText(_translate("MainWindow", "目標時間"))
        self.label_3.setText(_translate("MainWindow", "目前體重"))
        self.label_4.setText(_translate("MainWindow", "TDEE"))
        self.label_5.setText(_translate("MainWindow", "目標體重"))
        self.update_userinfo_Button.setText(_translate("MainWindow", "更新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "個人資料"))
        self.update_userinfo_Button.clicked.connect(self.update_userinfo)


    def update_userinfo(self):
        user_weight = float(self.user_weight.toPlainText())
        user_height = float(self.user_height.toPlainText())
        target_weight = float(self.target_weight.toPlainText())
        target_time = float(self.target_time.toPlainText())
        tdee = float(self.tdee.toPlainText())

        return user_height, user_weight, target_weight, target_time, tdee

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
