"""City class"""


class City:
    """City class"""

    def __init__(self, name="", population_of_city=0, percent_of_total_population=0.0):
        """Initialise a City object."""
        self.name = name
        self.population_of_city = population_of_city
        self.percent_of_total_population = percent_of_total_population

    def __str__(self):
        """Return string representation of data in a city."""
        return f"{self.name}, {self.population_of_city:,}, {self.percent_of_total_population}%"

    def __repr__(self):
        return str(self)
