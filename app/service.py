import bcrypt
from app.database import session, select
from app.models import User, Component, Category, Space


def check_password(password, hashed_password):
    return bcrypt.checkpw(bytes(password, 'UTF-8'), bytes(hashed_password, 'UTF-8'))


def get_user_by_email(email):
    stmnt = select(User).where(User.email == email).limit(1)
    user = session.scalar(stmnt)
    return user


def get_component_by_id(component_id):
    stmnt = select(Component).where(Component.id == component_id).limit(1)
    component = session.scalar(stmnt)
    return component


def get_category_by_id(category_id):
    stmnt = select(Category).where(Category.id == category_id).limit(1)
    category = session.scalar(stmnt)
    return category


def get_space_by_id(space_id):
    stmnt = select(Component).where(Space.id == space_id).limit(1)
    space = session.scalar(stmnt)
    return space

def get_all_categories():
    stmnt = select(Category)
    categories = session.scalars(stmnt)
    return categories

def get_all_spaces():
    stmnt = select(Space)
    spaces = session.scalars(stmnt)
    return spaces

def update_component(component):
    session.commit()
    return component
