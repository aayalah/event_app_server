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
    

    async def get(self, user_name: str, password: str) -> User_Model:
        print(user_name)
        print(password)
        stmt = select(User_Model).where(and_(User_Model.user_name == user_name, User_Model.password_hash == password))
        result =  await self.db.execute(stmt)
        print(result)
        user = result.scalar_one_or_none()
        print(user)
        return user