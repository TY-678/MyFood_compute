import asyncio
import asyncpg
from fastapi import HTTPException
from myfood_compute.config.env_setting import database_setting


connect = database_setting()


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
