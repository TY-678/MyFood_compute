from pydantic import BaseModel
from typing import Optional


class UserInfo(BaseModel):
    id: Optional[int] = 0
    height: float
    weight: float
    target_weight: float
    target_time: int
    tdee: float

    model_config = {"from_attributes": True}


class UserFoodHistory(BaseModel):
    food_id: int
    date: str

    model_config = {"from_attributes": True}


class UserFoodHistoryWithFoodInfo(BaseModel):
    id: int
    product: str
    calories: float
    carbohydrate: float
    protein: float
    fat: float
    sodium: float
    sugar: float

    model_config = {"from_attributes": True}
