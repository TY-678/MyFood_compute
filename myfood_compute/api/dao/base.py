import psycopg2
from myfood_compute.config.env_setting import env_setting


import asyncio
import asyncpg
from fastapi import HTTPException


connect = env_setting()


class BaseDao:
    async def __aenter__(self):
        try:
            self.conn = await asyncpg.connect(**connect.model_dump())
            return self
        except Exception as e:
            raise HTTPException(403, str(e))

    async def __aexit__(self, *args):
        await asyncio.gather(self.conn.close(timeout=10), return_exceptions=True)

    def __await__(self):
        return self.__aenter__().__await__()


# class DatabaseConnector:
#     def __init__(self):
#         self.connection = None
#         self.cursor = None
#         self.db_info = env_setting()

#     def sql_connect(self):
#         self.connection = psycopg2.connect(
#             host=self.db_info.host,
#             port=self.db_info.port,
#             user=self.db_info.user,
#             password=self.db_info.password,
#             database=self.db_info.database,
#         )
#         self.cursor = self.connection.cursor()

#     def sql_close(self):
#         self.cursor.close()
#         self.connection.commit()
#         self.connection.close()
