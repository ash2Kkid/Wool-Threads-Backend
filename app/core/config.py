import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    """
    Central configuration class for the backend.
    """

    PROJECT_NAME: str = "Wool Supply Chain Backend"

    # Firebase Config
    FIREBASE_KEY_PATH: str = os.getenv("FIREBASE_KEY_PATH", "firebase_key.json")

    # Security / Auth Config
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # General Environment
    ENV: str = os.getenv("ENV", "development")


# Global settings object
settings = Settings()