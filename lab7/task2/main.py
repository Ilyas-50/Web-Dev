from models import Vehicle, Car, Motorcycle


def main():
    vehicles = [
        Vehicle("Toyota", "Camry", 2020),
        Car("BMW", "X5", 2023, 4),
        Motorcycle("Yamaha", "MT-07", 2022, 689),
    ]

    for v in vehicles:
        print(v)
        print(v.info())
        print("honk:", v.honk())
        v.drive(150)
        print("after drive:", v.info())
        print("-" * 40)

    for v in vehicles:
        if isinstance(v, Car):
            print(v.open_trunk())
        elif isinstance(v, Motorcycle):
            print(v.wheelie())


if __name__ == "__main__":
    main()