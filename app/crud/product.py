from app.core.db import db
from app.schemas.product import ProductCreate

async def create_product(product: ProductCreate):
    result = await db.products.insert_one(product.model_dump())
    return str(result.inserted_id)

async def get_all_products():
    cursor = db.products.find()
    return [dict(p, id=str(p["_id"])) async for p in cursor]
