from app.core.db import db
from app.schemas.user import UserCreate
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.utils.security import hash_password

async def create_user(db, user: UserCreate):
    hashed_pw = hash_password(user.password)

    user_dict = user.model_dump()
    user_dict["password"] = hashed_pw  # tambahkan password_hash di DB

    result = await db["users"].insert_one(user_dict)
    return str(result.inserted_id)


async def get_user_by_email(db: AsyncIOMotorDatabase, email: str):
    return await db["users"].find_one({"email": email})

async def get_user_by_no_whatsapp(db: AsyncIOMotorDatabase, no_whatsapp: str):
    return await db["users"].find_one({"no_whatsapp": no_whatsapp})