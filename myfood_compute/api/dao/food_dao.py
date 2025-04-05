from myfood_compute.api.dao.base import BaseDao
from myfood_compute.api.schema.food_schema import ProductInfo


class FoodDao:

    def __init__(self):
        pass

    async def get_food(self, id: int):
        async with BaseDao() as db:
            food = await db.conn.fetchrow(
                """
                select id, product, calories, carbohydrate, protein, fat, sodium, sugar
                from food_list
                where id = $1;
                """,
                id,
            )
            return ProductInfo(**food) if food else None
