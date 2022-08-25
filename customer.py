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
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " +  self.get_name() + "\n"

        for each in self._rentals:
            # add frequent renter points
            frequent_renter_points += each.get_frequent_renter_points()

            # show figures for this rental&
            result += "\t" + each.get_movie().get_title() + "\t" + str(each.get_charge()) + "\n"
            total_amount += each.get_charge()

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result
