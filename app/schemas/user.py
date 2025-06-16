from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nama: str
    password: str
    no_whatsapp: str
    konfirmasi: bool = False

class UserModel(BaseModel):
    id: str
    nama: str
    password: str
    no_whatsapp: str

class UserOut(BaseModel):
    id: str
    nama: str
    no_whatsapp: str