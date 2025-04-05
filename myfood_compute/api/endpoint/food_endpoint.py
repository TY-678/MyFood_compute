from fastapi import APIRouter
from myfood_compute.api.bo.food_bo import FoodBo
from myfood_compute.api.schema.food_schema import ProductInfo


FoodRouter = APIRouter()
food_bo = FoodBo()


@FoodRouter.get("/food", response_model=ProductInfo)
async def get_food(id: int):
    return await food_bo.get_food(id)
