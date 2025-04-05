from myfood_compute.api.dao.base import BaseDao


async def create_table_food_list():
    async with BaseDao() as db:
        await db.conn.execute(
            """
            CREATE TABLE food_list (
            id serial4 NOT NULL,
            product varchar(20) NULL,
            calories numeric(5, 1) NULL,
            carbohydrate numeric(5, 1) NULL,
            protein numeric(5, 1) NULL,
            fat numeric(5, 1) NULL,
            sodium numeric(5, 1) NULL,
            sugar numeric(5, 1) NULL
            );"""
        )


async def create_food_info():
    async with BaseDao() as db:
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
            await db.conn.execute(
                """
                INSERT INTO public.food_list
                (id, product, calories, carbohydrate, protein, fat, sodium, sugar)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
                """,
                food,
            )


async def create_table_user_food_history():
    async with BaseDao() as db:
        await db.conn.execute(
            """
            CREATE TABLE user_food_history (
            "date" varchar(15) NULL,
	        id int4 NULL);
            """
        )


async def create_table_user_info():
    async with BaseDao() as db:
        await db.conn.execute(
            """
            id serial4 NOT NULL,
            height numeric(5, 1) NULL,
            weight numeric(5, 1) NULL,
            target_weight numeric(5, 1) NULL,
            target_time numeric(5, 1) NULL,
            tdee numeric(5, 1) NULL
            );"""
        )


async def create_user_info():
    async with BaseDao() as db:
        await db.conn.execute(
            """
            INSERT INTO user_info
            (height, weight, target_weight, target_time, tdee)
            VALUES (180, 80, 70, 90, 2700);
            """
        )


if __name__ == "__main__":
    import asyncio

    async def maint():
        await create_table_food_list()
        await create_food_info()
        await create_table_user_food_history()
        await create_table_user_info()
        await create_user_info()

    asyncio.run(maint())
