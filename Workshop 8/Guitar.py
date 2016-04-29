class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """ initialize a Guitar instance
        name: string, name of the guitar
        year: integer, year made
        cost: float, cost of guitar """
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        from datetime import date
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __str__(self):
        if self.is_vintage():
            return "Guitar {}: {:>20} ({}), : ${{:10,.2f} (vintage)"
        else:
            return "Guitar {}: {:>20} ({}), : ${{:10,.2f}"
