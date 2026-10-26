from fastapi import Path
from typing import Annotated
from fastapi import APIRouter

# для того, чтобы не внедрять постоянно app, можно использовать APIRouter()
# from src.simple_project.main import app
router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
    ]


@router.get("/latest/")
def get_latest_item() -> dict[str, dict[str, int | str]]:
    return {"item": {"id": 0, "name": "latest"}}


# в fastapi type hint из обычного python просто подсказки, но
# в FastAPI это валидация данных
# Annotated валидирует query-параметр с ограничениями
@router.get("/{item_id}/")
def get_item(item_id: Annotated[int, Path(ge=1, lt=10_000)]) -> dict[str, int]:
    return {"item": 2}
