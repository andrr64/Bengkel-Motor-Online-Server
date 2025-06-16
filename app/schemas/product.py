from pydantic import BaseModel

class ProductCreate(BaseModel):
    nama: str
    harga: float

class ProductOut(BaseModel):
    id: str
    nama: str
    harga: float
