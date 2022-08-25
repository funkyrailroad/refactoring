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
        this_amount = 0

        # determine amounts for self line
        if self.get_movie().get_price_code() == Movie("","").REGULAR:
            this_amount +=  2
            if self.get_days_rented() > 2:
                this_amount += (self.get_days_rented() - 2 ) * 1.5
        if self.get_movie().get_price_code() == Movie("","").NEW_RELEASE:
            this_amount += self.get_days_rented() * 3
        if self.get_movie().get_price_code() == Movie("","").CHILDRENS:
            this_amount +=  1.5
            if self.get_days_rented() > 3:
                this_amount += (self.get_days_rented() - 3 ) * 1.5
        return this_amount
