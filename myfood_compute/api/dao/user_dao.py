from myfood_compute.api.dao.base import BaseDao
from myfood_compute.api.schema.user_schema import (
    UserInfo,
    UserFoodHistory,
    UserFoodHistoryWithFoodInfo,
)


class UserHistoryDao:

    async def get_user_info(self) -> UserInfo:
        async with BaseDao() as db:
            user_info = await db.conn.fetchrow(
                """
                SELECT id, height, weight, target_weight, target_time, tdee
                FROM user_info 
                ORDER BY id DESC LIMIT 1;
                """
            )
            return UserInfo(**user_info) if user_info else None

    async def update_user_info(self, new_user_info: UserInfo):
        async with BaseDao() as db:
            await db.conn.fetchrow(
                """
                insert into user_info
                (height, weight, target_weight, target_time, tdee)
                values($1, $2, $3, $4, $5);
                """,
                new_user_info.height,
                new_user_info.weight,
                new_user_info.target_weight,
                new_user_info.target_time,
                new_user_info.tdee,
            )

    async def add_user_history(self, new_history: UserFoodHistory):
        async with BaseDao() as db:
            await db.conn.fetchrow(
                """
                INSERT INTO user_food_history (id, date)
                VALUES ($1, $2);
                """,
                new_history.food_id,
                new_history.date,
            )

    async def get_user_history(self, date: str) -> list[UserFoodHistoryWithFoodInfo]:
        async with BaseDao() as db:
            user_history = await db.conn.fetch(
                """
                select fl.id, fl.product, fl.calories, fl.carbohydrate, fl.protein, fl.fat, fl.sodium, fl.sugar
                from food_list fl
                left join user_food_history ufh
                on fl.id = ufh.id
                where ufh.date = $1;
                """,
                date,
            )

            return [UserFoodHistoryWithFoodInfo(**history) for history in user_history]
