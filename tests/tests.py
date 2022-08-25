import unittest

from customer import Customer
from movie import Movie
from rental import Rental


class Tests(unittest.TestCase):
    def setUp(self):
        self.bob = Customer("Bob")
        self.regular_movie = Movie("regular_movie", 0)
        self.new_release_movie = Movie("new_release_movie", 1)
        self.childrens_movie = Movie("childrens_movie", 2)

    def test_none(self):
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\nAmount owed is 0\nYou earned 0 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_regular_short(self):
        self.bob.add_rental(Rental(self.regular_movie, 1))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tregular_movie\t2\nAmount owed is 2\nYou earned 1 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_regular_long(self):
        self.bob.add_rental(Rental(self.regular_movie, 5))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tregular_movie\t6.5\nAmount owed is 6.5\nYou earned 1 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_childrens_short(self):
        self.bob.add_rental(Rental(self.childrens_movie, 1))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tchildrens_movie\t1.5\nAmount owed is 1.5\nYou earned 1 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_childrens_long(self):
        self.bob.add_rental(Rental(self.childrens_movie, 5))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tchildrens_movie\t4.5\nAmount owed is 4.5\nYou earned 1 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_new_release_short(self):
        self.bob.add_rental(Rental(self.new_release_movie, 1))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tnew_release_movie\t3\nAmount owed is 3\nYou earned 1 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_new_release_long(self):
        self.bob.add_rental(Rental(self.new_release_movie, 5))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tnew_release_movie\t15\nAmount owed is 15\nYou earned 2 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_all_short(self):
        self.bob.add_rental(Rental(self.childrens_movie, 1))
        self.bob.add_rental(Rental(self.new_release_movie, 1))
        self.bob.add_rental(Rental(self.regular_movie, 1))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tchildrens_movie\t1.5\n\tnew_release_movie\t3\n\tregular_movie\t2\nAmount owed is 6.5\nYou earned 3 frequent renter points'
        self.assertEqual(statement, gt_statement)

    def test_all_long(self):
        self.bob.add_rental(Rental(self.childrens_movie, 5))
        self.bob.add_rental(Rental(self.new_release_movie, 5))
        self.bob.add_rental(Rental(self.regular_movie, 5))
        statement = self.bob.statement()
        gt_statement = 'Rental Record for Bob\n\tchildrens_movie\t4.5\n\tnew_release_movie\t15\n\tregular_movie\t6.5\nAmount owed is 26.0\nYou earned 4 frequent renter points'
        self.assertEqual(statement, gt_statement)
