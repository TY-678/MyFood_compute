from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class ProductInfo(BaseModel):
    id: int
    product: str
    calories: float
    carbohydrate: float
    protein: float
    fat: float
    sodium: float
    sugar: float

    model_config = {"from_attributes": True}
