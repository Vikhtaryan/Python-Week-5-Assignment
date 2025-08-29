class Vehicle:
    def move(self):
        pass  # Abstract method placeholder


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


class Bike(Vehicle):
    def move(self):
        print("Pedaling 🚴")


# Example usage
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()
