class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Daewoo", "Lanos", 2017)

print(car1.get_info())
