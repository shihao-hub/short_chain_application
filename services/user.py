import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    @staticmethod
    async def get_user(session: AsyncSession, user_id: int):
        pass
