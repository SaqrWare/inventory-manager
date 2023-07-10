from app.database import Column, DeclarativeBase, Integer, String, Boolean, Date


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
    
class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(55), unique=True)
    password = Column(String(60))

class Component(Base):
    __tablename__ = 'component'
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    image = Column(String(300))
    qr_code = Column(String(60))
    description = Column(String())
    category_id = Column(Integer)
    space_id = Column(Integer)
    status = Column(Boolean)
    purchase_date = Column(Date)
    termination_date = Column(Date)