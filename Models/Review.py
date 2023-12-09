
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        restaurant.reviews.append(self)
        customer.reviews.append(self)
        Review.all_reviews.append(self)

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews
    
def main():
    
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Alice", "Smith")

    restaurant1 = Restaurant("Tasty Treats")
    restaurant2 = Restaurant("Burger Palace")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    # Example usage of the methods
    print(customer1.full_name())  
    print(restaurant2.average_star_rating())  
    print(customer2.num_reviews())  

if __name__ == '__main__':
    main()