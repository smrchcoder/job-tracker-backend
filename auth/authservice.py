from sqlalchemy.orm import Session
from fastapi import HTTPException
from .authmodel import UserCreate, UserLogin
from database import User
from .jwtservice import hash_password, verfiy_password, create_access_token
from datetime import timedelta

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

def loginUser(login_data: UserLogin, db:Session):
    user = db.query(User).filter(User.email==login_data.email).first()
    if user is None or verfiy_password(login_data.password, user.hashed_password) is False:
        return HTTPException(status_code=401, detail="Invalid email or password")
    data={"sub": user.email}
    # Example expiration: 30 minutes
    expires_delta = timedelta(minutes=30)
    access_token=create_access_token(data, expires_delta=expires_delta)
    return {"access_token": access_token, "token_type": "bearer"}
    
    



