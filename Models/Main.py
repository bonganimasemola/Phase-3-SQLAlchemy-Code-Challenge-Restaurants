#!/usr/bin/env python3

from sqlalchemy import (create_engine, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'Restaurant'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'Restaurant: {self.name}, '  \
               + f'{self.price} dollars' 
        

class Customers(Base):
    __tablename__ = 'Customers'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Customer: {self.name}'
    
    
    
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    # restaurant = Restaurant('Shicken Wangs Place')
    # session.add(restaurant)
    # session.commit()
    
    Shicken_Wangs_Place = Restaurant(name='Shicken Wangs Place', price=15)
    session.add(Shicken_Wangs_Place)
    session.commit()
    Rib_Shack = Restaurant(name='Rib Shack', price=18)
    session.add(Rib_Shack)
    session.commit()
    Extra_Ordinary_Ugali = Restaurant(name='ExtraOrdinary Ugali', price=35)
    session.add(Extra_Ordinary_Ugali)
    session.commit()
    Poly_Nyama_Choma = Restaurant(name='Poly Nyama Choma', price=12)
    session.add(Poly_Nyama_Choma)
    session.commit()
    
    restaurant = session.query(Restaurant).all()
    print(restaurant)
    
    John_Mbaru = Customers(name='John Mbaru')
    session.add(John_Mbaru)
    session.commit()
    Wangachi = Customers(name='Wangachi')
    session.add(Wangachi)
    session.commit()
    Mwangi_Ace = Customers(name='Mwangi Ace')
    session.add(Mwangi_Ace)
    session.commit()
    Sankofa_King = Customers(name='Sankofa King')
    session.add(Sankofa_King)
    session.commit()
    Sean_Carter = Customers(name='Sean Carter')
    session.add(Sean_Carter)
    session.commit()
    Kendrick_Lamar = Customers(name='Kendrick Lamar')
    session.add(Kendrick_Lamar)
    session.commit()
    
    customers = session.query(Customers).all()
    print(customers)
    
    
   