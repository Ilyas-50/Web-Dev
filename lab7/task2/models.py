class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, km):
        self.mileage += km
        return f"{self.brand} {self.model} drove {km} km."

    def info(self):
        return f"{self.year} {self.brand} {self.model}, mileage: {self.mileage} km"

    def honk(self):
        return "Beep!"

    def __str__(self):
        return f"Vehicle({self.brand}, {self.model}, {self.year})"


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def honk(self):
        return f"{self.brand} {self.model}: Honk honk!"

    def open_trunk(self):
        return f"{self.brand} {self.model}: trunk is open"

    def __str__(self):
        return f"Car({self.brand}, {self.model}, {self.year}, doors={self.num_doors})"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def honk(self):
        return f"{self.brand} {self.model}: Beeeep! ({self.engine_cc}cc)"

    def wheelie(self):
        return f"{self.brand} {self.model} pulls a wheelie!"

    def __str__(self):
        return f"Motorcycle({self.brand}, {self.model}, {self.year}, cc={self.engine_cc})"