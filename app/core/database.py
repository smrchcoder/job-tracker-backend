from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import POSTGRES_URL

POSTGRES_SQL_URL = POSTGRES_URL
engine = create_engine(POSTGRES_SQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
