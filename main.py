from customer import Customer
from movie import Movie
from rental import Rental

if __name__ == "__main__":
    bob = Customer("Bob")
    movie_1 = Movie("movie_1", 0)
    rental_1 = Rental(movie_1, 2)
    bob.add_rental(rental_1)
    print(bob.statement())
