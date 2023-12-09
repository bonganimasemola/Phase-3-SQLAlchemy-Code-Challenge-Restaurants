

from sqlalchemy import (create_engine, desc, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint, Column, Integer, String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    reviews = relationship('Review', back_populates='restaurant')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Restaurant: {self.name}, ' \
               + f'{self.price} dollars'
               
    def reviews(self):
        return self.reviews

    def customers(self):
        return [review.customer for review in self.reviews]
    
    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(desc(cls.price)).first()

    def all_reviews(self):
        reviews = [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
                   for review in self.reviews]
        return reviews


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    reviews = relationship('Review', back_populates='customer')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Customer: {self.name}'
    
    def reviews(self):
        return self.reviews

    def restaurants(self):
        return [review.restaurant for review in self.reviews]
    
    def full_name(self):
        return self.name

    def favorite_restaurant(self):
        highest_rated_review = max(self.reviews, key=lambda x: x.star_rating, default=None)
        if highest_rated_review:
            return highest_rated_review.restaurant
        else:
            return None

    def add_review(self, restaurant, rating):
        new_review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        self.reviews.append(new_review)

    def delete_reviews(self, restaurant):
        for review in self.reviews:
            if review.restaurant == restaurant:
                self.reviews.remove(review)
    
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def __init__(self, star_rating, restaurant, customer):
        self.star_rating = star_rating
        self.restaurant = restaurant
        self.customer = customer

    def __repr__(self):
        return f'Review: Rating - {self.star_rating}'
    
    
if __name__ == '__main__':
    #engine = create_engine('sqlite:///migrations_test.db')
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
    
    John_Mbaru = Customer(name='John Mbaru')
    session.add(John_Mbaru)
    session.commit()
    Wangachi = Customer(name='Wangachi')
    session.add(Wangachi)
    session.commit()
    Mwangi_Ace = Customer(name='Mwangi Ace')
    session.add(Mwangi_Ace)
    session.commit()
    Sankofa_King = Customer(name='Sankofa King')
    session.add(Sankofa_King)
    session.commit()
    Sean_Carter = Customer(name='Sean Carter')
    session.add(Sean_Carter)
    session.commit()
    Kendrick_Lamar = Customer(name='Kendrick Lamar')
    session.add(Kendrick_Lamar)
    session.commit()
    
    customers = session.query(Customer).all()
    print(customers)
    
    review1 = Review(star_rating=4, restaurant=Shicken_Wangs_Place, customer=John_Mbaru)
    review2 = Review(star_rating=5, restaurant=Extra_Ordinary_Ugali, customer=Wangachi)
    review3 = Review(star_rating=3, restaurant=Poly_Nyama_Choma, customer=Mwangi_Ace)

    session.add_all([review1, review2, review3])
    session.commit()

    restaurants = session.query(Restaurant).all()
    print(restaurants)

    customers = session.query(Customer).all()
    print(customers)

    reviews = session.query(Review).all()
    print(reviews)
    
    session.query(Customer).first().restaurants
    
    ## Object Relationship Methods
    
    first_customer_restaurants = session.query(Customer).first().restaurants()
    print("Restaurants for the first customer:", first_customer_restaurants)

    first_review_customer = session.query(Review).first().customer()
    print("Customer for the first review:", first_review_customer)
    
    ## Aggregate and Relationship Methods
    
    fanciest_restaurant = Restaurant.fanciest(session)
    print("Fanciest Restaurant:", fanciest_restaurant)

    first_customer = session.query(Customer).first()
    print("Full Name:", first_customer.full_name())
    print("Favorite Restaurant:", first_customer.favorite_restaurant())

    new_restaurant = Restaurant(name='New Restaurant', price=25)
    session.add(new_restaurant)
    session.commit()

    first_customer.add_review(new_restaurant, 4)
    print("Reviews after adding a new review:", first_customer.reviews)

    first_customer.delete_reviews(new_restaurant)
    print("Reviews after deleting reviews for the new restaurant:", first_customer.reviews)
   