import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///memora_al.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")

    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        """Sen Memora Al'in yapay zeka seyahat asistanisin.
Kullanicinin seyahat tercihlerini, gitmek istedigi yeri, butcesini
ve seyahat suresini dikkate alarak kisisellestirilmis seyahat
planlari olusturursun. Turkce, anlasilir ve samimi bir dille konus."""
    )

    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}