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
