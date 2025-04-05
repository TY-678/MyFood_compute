from fastapi import APIRouter
from myfood_compute.api.bo.user_history_bo import UserHistoryBo
from myfood_compute.api.schema.user_schema import (
    UserInfo,
    UserFoodHistory,
    UserFoodHistoryWithFoodInfo,
)

UserHistoryRouter = APIRouter()
user_bo = UserHistoryBo()


@UserHistoryRouter.get("/info", response_model=UserInfo)
async def get_user_info():
    return await user_bo.get_user_info()


@UserHistoryRouter.put("/info")
async def update_user_info(new_user_info: UserInfo):
    return await user_bo.update_user_info(new_user_info)


@UserHistoryRouter.post("/history")
async def add_user_history(new_history: UserFoodHistory):
    return await user_bo.add_user_history(new_history)


@UserHistoryRouter.get("/history", response_model=list[UserFoodHistoryWithFoodInfo])
async def get_user_history(date: str):
    return await user_bo.get_user_history(date)
