from abc import ABC, abstractmethod

class Price(ABC):
    @abstractmethod
    def get_price_code(self):
        pass

    @abstractmethod
    def get_charge(self, days_rented):
        pass

    @abstractmethod
    def get_frequent_renter_points(self, days_rented):
        pass


class ChildrensPrice(Price):
    def get_price_code(self):
        return Movie.CHILDRENS

    def get_charge(self, days_rented):
        this_amount =  1.5
        if days_rented > 3:
            this_amount += (days_rented - 3 ) * 1.5
        return this_amount

    def get_frequent_renter_points(self, days_rented):
        return 1


class NewReleasePrice(Price):
    def get_price_code(self):
        return Movie.NEW_RELEASE

    def get_charge(self, days_rented):
        this_amount = days_rented * 3
        return this_amount

    def get_frequent_renter_points(self, days_rented):
        frequent_renter_points = 1
        if (days_rented > 1) :
            frequent_renter_points += 1
        return frequent_renter_points


class RegularPrice(Price):
    def get_price_code(self):
        return Movie.REGULAR

    def get_charge(self, days_rented):
        this_amount =  2
        if days_rented > 2:
            this_amount += (days_rented - 2 ) * 1.5
        return this_amount

    def get_frequent_renter_points(self, days_rented):
        return 1


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
        return self._price.get_frequent_renter_points(days_rented)
