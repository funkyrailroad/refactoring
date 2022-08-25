from movie import Movie
from rental import Rental

class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        self._rentals.append(arg)

    def get_name(self):
        return self._name

    def statement(self):
        result = "Rental Record for " +  self.get_name() + "\n"

        for each in self._rentals:
            # show figures for this rental&
            result += "\t" + each.get_movie().get_title() + "\t" + str(each.get_charge()) + "\n"

        # add footer lines
        result += "Amount owed is " + str(self.get_total_charge()) + "\n"
        result += "You earned " + str(self.get_total_frequent_renter_points()) + " frequent renter points"
        return result

    def get_total_charge(self):
        total_amount = 0
        for each in self._rentals:
            total_amount += each.get_charge()
        return total_amount

    def get_total_frequent_renter_points(self):
        frequent_renter_points = 0
        for each in self._rentals:
            frequent_renter_points += each.get_frequent_renter_points()
        return frequent_renter_points
