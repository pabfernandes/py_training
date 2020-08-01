# This will be the makers class from the cars.
# Each class will have some common attributes

class CarMaker:
    total_makers = 0
    all_makers = {}

    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.total_makers += 1
        self.all_makers[name] = country

    def add_nickname(self, nickname):
        '''
        This method adds a nickname to the
        maker
        '''
        self.nickname = nickname

    def add_year(self, year):
        '''
        Adds a year of foundation to the maker
        '''
        self.year = year

