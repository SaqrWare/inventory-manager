import bcrypt
from app.database import session, select
from app.models import User


def check_password(password, hashed_password):
    return bcrypt.checkpw(bytes(password, 'UTF-8'), bytes(hashed_password, 'UTF-8'))


def get_user_by_email(email):
    stmnt = select(User).where(User.email == email).limit(1)
    user = session.scalar(stmnt)
    return user
