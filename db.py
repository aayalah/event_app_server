from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from collections.abc import AsyncGenerator
import os
from dotenv import load_dotenv

load_dotenv()

dsn = f"postgresql+asyncpg://postgres:postgres@localhost:5455/{os.getenv('POSTGRES_DB', 'postgres')}"
engine = create_async_engine(dsn, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session