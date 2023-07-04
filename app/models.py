from app.database import Column, DeclarativeBase, Integer, String


class Base(DeclarativeBase):
    pass

# Category Model
class Category (Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

# Space Model
class Space (Base):
    __tablename__ = 'space'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    