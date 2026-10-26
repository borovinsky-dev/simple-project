from fastapi import FastAPI
from uvicorn import run

from src.simple_project.items_view import router as items_router
from src.simple_project.users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


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
