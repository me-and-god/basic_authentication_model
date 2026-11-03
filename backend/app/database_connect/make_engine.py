"""
 This file is to make the engine and then connect the database url and then make
 session 
"""


from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.database_connect.db import DBUrl


if not DBUrl:
    raise RuntimeError("Database string not found.")

engine = create_async_engine(DBUrl)

sessionLocal = async_sessionmaker(
                bind=engine,
                expire_on_commit=False
            )



# database session initiates
async def get_db():

    async with sessionLocal() as session: 
        yield session