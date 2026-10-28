from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager

from simple_project.api_v1.products import router as products_router_v1
from simple_project.core.db_helper import db_helper
from simple_project.items_view import router as items_router
from simple_project.models import Base
from simple_project.users.views import router as users_router

from simple_project.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
# подключение роутов
app.include_router(items_router)
app.include_router(users_router)
app.include_router(products_router_v1, prefix=settings.api_v1_prefix)


# view - функция
@app.get("/")
def hello_index():
    # В Python мы работаем со словарями, но в браузере он будет
    # преобразован в json-объект
    return {
        "message": "Hello Fast API",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().upper()
    return {"message": f"Hello {name}"}


@app.post("/calc/add/")
def add(a: int, b: int):
    return {"a": a, "b": b, "result": a + b}


if __name__ == "__main__":
    run("simple_project.main:app", reload=True)
