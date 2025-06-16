from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate
from app.crud.user import create_user
from app.core.db import db
from app.crud.user import get_user_by_email, get_user_by_no_whatsapp
from app.utils.whatsapp_token import generate_whatsapp_token, verify_whatsapp_token
from app.core.twilio import send_whatsapp_message

router = APIRouter()

@router.post("/users")
async def register_user(user: UserCreate):
    existing_user = await get_user_by_no_whatsapp(db, user.no_whatsapp)
    if existing_user:
        raise HTTPException(status_code=400, detail="Nomor WhatsApp sudah terdaftar")

    # 1. Simpan user dulu
    inserted_id = await create_user(db, user)

    # 2. Generate token & link verifikasi
    token = generate_whatsapp_token(user.no_whatsapp)
    verification_link = f"http://localhost:8000/api/v1/users/verify?token={token}"
    
    body = (
        f"Selamat datang {user.nama}! Silakan klik link berikut untuk verifikasi nomor WhatsApp Anda:\n{verification_link}"
    )

    send_status = send_whatsapp_message(
        to=f"whatsapp:{user.no_whatsapp}",
        body=body
    )

    if not send_status:
        await db["users"].delete_one({"_id": inserted_id})
        raise HTTPException(status_code=500, detail="Gagal mengirim pesan verifikasi. Registrasi dibatalkan.")
    
    return {"message": "Registrasi berhasil. Silakan cek WhatsApp untuk verifikasi."}

@router.get("/users/verify")
async def verify_no_whatsapp(token: str):
    no_wa = verify_whatsapp_token(token)
    
    if not no_wa:
        raise HTTPException(status_code=400, detail="Token tidak valid atau kadaluarsa")

    user = await get_user_by_no_whatsapp(db, no_wa)
    
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    await db["users"].update_one(
        {"no_whatsapp": no_wa},
        {"$set": {"konfirmasi": True}}
    )

    return {"message": f"Akun berhasil diverifikasi ✅"}
