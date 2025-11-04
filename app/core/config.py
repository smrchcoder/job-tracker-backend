import os

# Database configuration
POSTGRES_URL = os.getenv(
    "POSTGRES_URL", "postgresql://user123:Password123@localhost:5432/myapp_db"
)

# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
