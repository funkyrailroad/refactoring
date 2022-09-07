from abc import ABC, abstractmethod

class Price(ABC):
    @abstractmethod
    def get_price_code(self):
        pass

    def get_charge(self, days_rented):
        this_amount = 0

        # determine amounts for self line
        if self.get_price_code() == Movie.REGULAR:
            this_amount +=  2
            if days_rented > 2:
                this_amount += (days_rented - 2 ) * 1.5
        if self.get_price_code() == Movie.NEW_RELEASE:
            this_amount += days_rented * 3
        if self.get_price_code() == Movie.CHILDRENS:
            this_amount +=  1.5
            if days_rented > 3:
                this_amount += (days_rented - 3 ) * 1.5
        return this_amount


class ChildrensPrice(Price):
    def get_price_code(self):
        return Movie.CHILDRENS


class NewReleasePrice(Price):
    def get_price_code(self):
        return Movie.NEW_RELEASE


class RegularPrice(Price):
    def get_price_code(self):
        return Movie.REGULAR


class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        # NOTE: note sure how to access these class constants without instantiating object
        self._title = title
        self.set_price_code(price_code)

    def get_price_code(self):
        return self._price.get_price_code()

    def set_price_code(self, arg):
        if arg == self.REGULAR:
            self._price = RegularPrice()
        elif arg == self.CHILDRENS:
            self._price = ChildrensPrice()
        elif arg == self.NEW_RELEASE:
            self._price = NewReleasePrice()
        else:
            raise NotImplementedError

    def get_title(self):
        return self._title

    def get_charge(self, days_rented):
        return self._price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented):
        # add frequent renter points
        frequent_renter_points = 1
        # add bonus for a two day new release rental
        if ((self.get_price_code() == self.NEW_RELEASE) and
                (days_rented > 1)) :
            frequent_renter_points += 1
        return frequent_renter_points
