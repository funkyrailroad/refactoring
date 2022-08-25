from movie import Movie

class Rental:
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie

    def get_charge(self):
        return self.get_movie().get_charge(self.get_days_rented())

    def get_frequent_renter_points(self):
        # add frequent renter points
        frequent_renter_points = 1
        # add bonus for a two day new release rental
        if ((self.get_movie().get_price_code() == Movie("","").NEW_RELEASE) and
                (self.get_days_rented() > 1)) :
            frequent_renter_points += 1
        return frequent_renter_points
