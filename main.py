from models.books import Book
from contextlib import asynccontextmanager
from database import engine, Model
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    print("База данных готова к работе")
    yield
    print("Выключение сервера")

app = FastAPI(lifespan=lifespan)
#app.include_router(tasks_router)
