import requests
from fastapi import File, UploadFile
from url import url
from myfood_compute.api.schema.user_schema import (
    UserInfo,
    UserFoodHistory,
    UserFoodHistoryWithFoodInfo,
)
from myfood_compute.api.schema.food_schema import ProductInfo

BACKEND_URL = url


def get_user_info() -> UserInfo:
    url = f"{BACKEND_URL}/user/info"
    response = requests.get(url)
    return UserInfo(**response.json())


def update_user_info(new_user_info: UserInfo) -> None:
    url = f"{BACKEND_URL}/user/info"
    response = requests.put(url, json=new_user_info.model_dump())
    return response.json()


def add_user_history(new_history: UserFoodHistory) -> None:
    url = f"{BACKEND_URL}/user/history"
    response = requests.post(url, json=new_history.model_dump())
    return response.json()


def get_user_history(date) -> list[UserFoodHistoryWithFoodInfo]:
    url = f"{BACKEND_URL}/user/history?date={date}"
    response = requests.get(url)
    return [UserFoodHistoryWithFoodInfo(**history) for history in response.json()]


def get_food(id: int) -> ProductInfo:
    url = f"{BACKEND_URL}/food/food?id={id}"
    response = requests.get(url)
    return ProductInfo(**response.json())


def upload_image(file: UploadFile = File(...)):
    url = f"{BACKEND_URL}/upload"
    response = requests.post(url, file=file)
    return response.json()
