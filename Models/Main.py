#!/usr/bin/env python3

from sqlalchemy import (create_engine, desc,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'Restaurant'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    def __init__(self):
        pass
    
    def __repr__(self):
        pass
        return f'()
        

class Customers(Base):
    __tablename__ = 'Customers'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    def __init__(self):
        pass
        
    def __repr__(self):
        pass
        return f'()
    
    
    
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    restaurant = Restaurant()
    session.add()
    session.commit()
    
    
    customers = Customers()
    session.add()
    session.commit()