from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import db_settings as s

SQLALCHEMY_DATABASE_URL = (f'postgresql+asyncpg://{s.DB_USER}:{s.DB_PASSWORD}'
                           f'@{s.DB_HOST}:{s.DB_PORT}/{s.DB_NAME}')

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()
