from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from simple_project.models.product import Product

# импорт внутри пакета
from .shemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    stat = select(Product).order_by(Product.id)
    result: Result = await session.execute(stat)
    products = result.scalars().all()
    return list(products)


async def get_product_by_id(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_upddate: ProductUpdate,
    partial: bool = False,
) -> Product:
    for name, value in product_upddate.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def update_product_partial(
    session: AsyncSession,
    product: Product,
    product_upddate_partial: ProductUpdatePartial,
) -> Product:
    product_upddate_partial.model_dump(exclude_unset=True)
    for name, value in product_upddate_partial.items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
