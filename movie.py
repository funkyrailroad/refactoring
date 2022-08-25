class Movie:
    def __init__(self, title, price_code):
        # NOTE: note sure how to access these class constants without instantiating object
        self.CHILDRENS = 2
        self.REGULAR = 0
        self.NEW_RELEASE = 1
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title

    def get_charge(self, days_rented):
        this_amount = 0

        # determine amounts for self line
        if self.get_price_code() == self.REGULAR:
            this_amount +=  2
            if days_rented > 2:
                this_amount += (days_rented - 2 ) * 1.5
        if self.get_price_code() == self.NEW_RELEASE:
            this_amount += days_rented * 3
        if self.get_price_code() == self.CHILDRENS:
            this_amount +=  1.5
            if days_rented > 3:
                this_amount += (days_rented - 3 ) * 1.5
        return this_amount
