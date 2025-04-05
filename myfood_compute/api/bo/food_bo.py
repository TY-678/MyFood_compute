from myfood_compute.api.dao.food_dao import FoodDao
from myfood_compute.api.schema.food_schema import ProductInfo


class FoodBo:

    async def get_food(self, id: int) -> ProductInfo:
        dao = FoodDao()
        return await dao.get_food(id)
