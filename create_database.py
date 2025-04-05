import psycopg2

# 建立資料庫與資料表

# connection = psycopg2.connect(
#     host="localhost",
#     port="5432",
#     user="ty",
#     password="tymacminipassword",
#     dbname="my_food",  # 預設連接到 postgres 資料庫
# )

# connection.autocommit = True
# cursor = connection.cursor()

# # 建立 MyFood 資料庫
# cursor.execute("CREATE DATABASE MyFood;")
# connection.close()

# 連接到 MyFood 資料庫
connection = psycopg2.connect(
    host="x",
    port="x",
    user="x",
    password="x",
    dbname="x",
)
cursor = connection.cursor()

# 建立 food_list 資料表
cursor.execute(
    """
CREATE TABLE food_list (
    ID SERIAL PRIMARY KEY,
    Product VARCHAR(20),
    Calories DECIMAL(5,1),
    Carbohydrate DECIMAL(5,1),
    Protein DECIMAL(5,1),
    Fat DECIMAL(5,1),
    Sodium DECIMAL(5,1),
    Sugar DECIMAL(5,1)
);
"""
)

# 插入 food_list 資料
food_list = [
    (0, "Tuna_Rice", 188.0, 32.0, 5.0, 4.3, 195.0, 0.8),
    (1, "Chicken_Rice", 186.0, 33.0, 5.4, 3.5, 326.0, 0.5),
    (2, "Pudding", 110.0, 18.7, 2.1, 3.0, 60.0, 16.0),
    (3, "Dumplings", 456.0, 39.7, 15.0, 26.3, 1471.0, 4.1),
    (4, "Milk_Tea", 156.0, 32.0, 1.6, 2.4, 38.0, 32.0),
    (5, "Soy_Milk", 263.0, 28.8, 15.8, 9.4, 122.0, 21.6),
    (6, "Curry_Rice", 709.0, 114.5, 17.9, 20.0, 1087.0, 7.4),
    (7, "Bolognese", 506.0, 73.1, 24.5, 12.6, 1157.0, 12.2),
]
for food in food_list:
    cursor.execute(
        """
    INSERT INTO food_list (ID, Product, Calories, Carbohydrate, Protein, Fat, Sodium, Sugar)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """,
        food,
    )

# 建立 user_food_history 資料表
cursor.execute(
    """
CREATE TABLE user_food_history (
    Date VARCHAR(15),
    ID INT
);
"""
)

# 建立 user_info 資料表
cursor.execute(
    """
CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    height DECIMAL(5,1),
    weight DECIMAL(5,1),
    target_weight DECIMAL(5,1),
    target_time DECIMAL(5,1),
    tdee DECIMAL(5,1)
);
"""
)

# 插入 user_info 資料
cursor.execute(
    """
INSERT INTO user_info (height, weight, target_weight, target_time, tdee)
VALUES (180, 80, 70, 90, 2700);
"""
)

cursor.close()
connection.commit()
connection.close()
