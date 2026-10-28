from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductBase):
    name: str | None
    description: str | None
    price: int | None


# для возвращения данных
class Product(ProductBase):
    # позволяет парсить данные
    model_config = ConfigDict(from_attributes=True)
    id: int
