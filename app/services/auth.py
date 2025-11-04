from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt

from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.dependencies import get_db

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verfiy_password(entered_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(entered_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return (
            payload
            if payload.get("exp") >= datetime.now(timezone.utc).timestamp()
            else None
        )
    except jwt.JWTError:
        return None


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = decode_access_token(token)
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return {"username": user.username, "email": user.email}


def createUser(user: UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        dob=user.dob,
        phone=user.phone,
        currentCompany=user.currentCompany,
        experience=user.experience,
        skills=",".join(user.skills) if user.skills else None,
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"username": new_user.username, "email": new_user.email}
    except Exception as e:
        db.rollback()
        print(f"Error creating user: {e}")
        return None
    finally:
        db.close()


def loginUser(login_data: UserLogin, db: Session):
    user = db.query(User).filter(User.email == login_data.email).first()
    if (
        user is None
        or verfiy_password(login_data.password, user.hashed_password) is False
    ):
        return HTTPException(status_code=401, detail="Invalid email or password")
    data = {"sub": user.email}
    expires_delta = timedelta(minutes=30)
    access_token = create_access_token(data, expires_delta=expires_delta)
    return {"access_token": access_token, "token_type": "bearer"}
