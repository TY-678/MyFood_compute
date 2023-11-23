# 建立資料庫與資料表
import mysql.connector


connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='xxxx',
            password='xxxxx'
            )

cursor = connection.cursor()

cursor.execute(f"create database `MyFood`;")
cursor.execute(f"use `MyFood`;")

cursor.execute(f"create table `food_list`(\
               `ID` int primary key,\
               `Product` varchar(20),\
               `Calories` decimal(5,1),\
               `Carbohydrate` decimal(5,1),\
               `Protein` decimal(5,1),\
               `Fat` decimal(5,1),\
               `Sodium` decimal(5,1),\
               `Sugar` decimal(5,1)\
               );")

food_list = [(0, 'Tuna_Rice', 188.0, 32.0, 5.0, 4.3, 195.0, 0.8),
             (1, 'Chicken_Rice', 186.0, 33.0, 5.4, 3.5, 326.0, 0.5),
             (2, 'Pudding', 110.0, 18.7, 2.1, 3.0, 60.0, 16.0),
             (3, 'Dumplings', 456.0, 39.7, 15.0, 26.3, 1471.0, 4.1)
             (4, 'Milk_Tea', 156.0, 32.0, 1.6, 2.4, 38.0, 32.0),
             (5, 'Soy_Milk', 263.0, 28.8, 15.8, 9.4, 122.0, 21.6),
             (6, 'Curry_Rice', 709.0, 114.5, 17.9, 20.0, 1087.0, 7.4),
             (7, 'Bolognese', 506.0, 73.1, 24.5, 12.6, 1157.0, 12.2)
]
for food in (food_list):
    cursor.execute(f"insert into `food_list` values {food};")



cursor.execute(f"create table `user_food_history`(\
               `Date` varchar(15),\
               `ID` int\
               );")


    
cursor.execute(f"create table `user_info`(\
               `id` INT AUTO_INCREMENT PRIMARY KEY,\
               `height` decimal(5,1),\
               `weight` decimal(5,1),\
               `target_weight` decimal(5,1),\
               `target_time` decimal(5,1),\
               `tdee` decimal(5,1)\
               );")
    

cursor.close()
connection.commit()
connection.close()


