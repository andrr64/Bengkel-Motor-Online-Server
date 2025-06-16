from pydantic_settings import BaseSettings  # <- ganti ini!

class Settings(BaseSettings):
    MONGODB_URL: str
    DB_NAME: str
    SECRET_KEY_FOR_EMAIL: str
    SECRET_KEY: str
    JWT_ALGORITHM: str 
    MJ_API_KEY: str
    MJ_API_SECRET: str
    MJ_FROM_EMAIL: str
    
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str
    
    class Config:
        env_file = ".env"

settings = Settings()
