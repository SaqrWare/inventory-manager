from sqlalchemy import Boolean, Column, Integer, String, create_engine, select, Double, Date
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine('sqlite:///database.db')

session = Session(engine)