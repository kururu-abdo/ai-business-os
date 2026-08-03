from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

class CartItem(Base):
    __tablename__ = "cart_items"

    id =  Column(Integer , primary_key=True) 
    user_id = Column(Integer) 
    item_name = Column(String)
    quantity = Column(Integer , default=1)


engine = create_engine('sqlite:///shop.db')
session_local = sessionmaker(bind=engine)

Base.metadata.create_all(engine)