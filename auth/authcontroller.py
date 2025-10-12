from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from .authmodel import UserCreate, UserLogin
from .authservice import createUser, loginUser
from .jwtservice import get_current_user

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/register')
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    return createUser(user, db)

@auth_router.post('/login')  # Fixed missing slash
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):
    """
    Login an existing user.
    """
    return loginUser(login_data, db)

@auth_router.get('/test')
def test(currentuser: dict = Depends(get_current_user)):
    """
    Get details of the currently logged-in user.
    """
    print(currentuser)
    return currentuser  # Return a dict, not pass

@auth_router.post('/logout')
def logout_user():
    """
    Logout the currently logged-in user.
    """
    return {"message": "Logged out successfully"}