from fastapi import APIRouter
from app.schemas.product import ProductCreate
from app.crud.product import create_product, get_all_products

router = APIRouter()

@router.post("/products")
async def create(product: ProductCreate):
    product_id = await create_product(product)
    return {"product_id": product_id}

@router.get("/products")
async def list_all():
    return await get_all_products()
