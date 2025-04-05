from myfood_compute.api.dao.user_dao import UserHistoryDao
from myfood_compute.api.schema.user_schema import (
    UserInfo,
    UserFoodHistory,
    UserFoodHistoryWithFoodInfo,
)


class UserHistoryBo:

    async def get_user_info(self) -> UserInfo:
        dao = UserHistoryDao()
        return await dao.get_user_info()

    async def update_user_info(self, new_user_info):
        dao = UserHistoryDao()
        return await dao.update_user_info(new_user_info)

    async def add_user_history(self, new_history: UserFoodHistory):
        dao = UserHistoryDao()
        return await dao.add_user_history(new_history)

    async def get_user_history(self, date: str) -> list[UserFoodHistoryWithFoodInfo]:
        dao = UserHistoryDao()
        return await dao.get_user_history(date)
