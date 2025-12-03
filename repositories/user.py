from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from models.user import User as User_Model

class User:
    def __init__(self, db: AsyncSession):
        self.db = db 

    async def create(self, full_name: str, user_name: str, email: str, password_hash: str) -> User_Model:
        user = User_Model(full_name=full_name, user_name=user_name, email=email, password_hash=password_hash)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    

    async def get(self, email: str) -> User_Model:
        stmt = select(User_Model).where(User_Model.email == email)
        result =  await self.db.execute(stmt)
        user = result.scalar_one_or_none()
        return user