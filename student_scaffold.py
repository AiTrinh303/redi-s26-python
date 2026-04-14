# ──────────────────────────────────────────────
#  VEHICLE RENTAL — CODING CHALLENGE
#  Student Scaffold File
#  Instructions: implement all classes below.
#  Do NOT modify main() at the bottom.
# ──────────────────────────────────────────────

from abc import ABC, abstractmethod

class Vehicle(ABC):
    _count = 0

    def __init__(self, make, model, daily_rate):
        # Ex1: set attributes using setters, increment _count
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        Vehicle._count += 1

    # Ex2: add @property and setter for make, model, daily_rate
    #           daily_rate setter must raise ValueError if value <= 0
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if value <= 0:
            raise ValueError("Daily rate must be positive.")
        self._daily_rate = value

    @abstractmethod
    def calculate_rental_cost(self, days):
        # Ex3: declare abstract — no body needed here
        pass

    def __str__(self):
        # Ex1: return human-readable string
        # Expected format: "Vehicle: <make> <model> | Rate: €<rate>/day"
        return f"Vehicle: {self.make} {self.model} | Rate: €{self.daily_rate:.2f}/day"

    def __repr__(self):
        # Ex1: return developer-friendly string
        # Expected format: "Vehicle(make='...', model='...', daily_rate=...)"
        return f"Vehicle(make='{self.make}', model='{self.model}', daily_rate={self.daily_rate})"

    def __del__(self):
        # Ex4: decrement _count
        Vehicle._count -= 1


class Car(Vehicle):
    def __init__(self, make, model, daily_rate, num_doors):
        # Ex3: call super().__init__, store num_doors
        super().__init__(make, model, daily_rate)
        self.num_doors = num_doors

    def calculate_rental_cost(self, days):
        # Ex3: return days * daily_rate
        return days * self.daily_rate

    def __str__(self):
        # Ex3: include num_doors in output
        # Expected format: "Car: <make> <model> | Doors: <n> | Rate: €<rate>/day"
        return f"Car: {self.make} {self.model} | Doors: {self.num_doors} | Rate: €{self.daily_rate:.2f}/day"


class Motorcycle(Vehicle):
    def __init__(self, make, model, daily_rate, has_sidecar):
        # Ex3: call super().__init__, store has_sidecar
        super().__init__(make, model, daily_rate)
        self.has_sidecar = has_sidecar

    def calculate_rental_cost(self, days):
        # Ex3: return days * daily_rate * 0.85  (15% discount)
        return days * self.daily_rate * 0.85

    def __str__(self):
        # Ex3: include has_sidecar in output (show "Yes"/"No")
        # Expected format: "Motorcycle: <make> <model> | Sidecar: Yes/No | Rate: €<rate>/day"
        sidecar_str = "Yes" if self.has_sidecar else "No"
        return f"Motorcycle: {self.make} {self.model} | Sidecar: {sidecar_str} | Rate: €{self.daily_rate:.2f}/day"


class ElectricScooter(Vehicle):
    def __init__(self, make, model, daily_rate, battery_pct):
        # Ex4: call super().__init__, store battery_pct via setter
        super().__init__(make, model, daily_rate)
        self.battery_pct = battery_pct

    # Ex4: add @property + setter for battery_pct
    #           setter must clamp value between 0 and 100
    @property
    def battery_pct(self):
        return self._battery_pct

    @battery_pct.setter
    def battery_pct(self, value):
        # if value < 0:
        #     raise ValueError("Battery percentage must be a positive number.")
        # if value > 100:
        #     raise ValueError("Battery percentage must not exceed 100.")
        # self._battery_pct = value
        self._battery_pct = max(0, min(100, value))


    def charge(self):
        # Ex4: set battery_pct to 100
        self.battery_pct = 100

    def is_charged(self):
        # Ex4: return True if battery_pct >= 80
        return self.battery_pct >= 80

    def calculate_rental_cost(self, days):
        # Ex4: return days * daily_rate * 0.9  (10% eco-discount)
        return days * self.daily_rate * 0.9

    def __str__(self):
        # Ex4: include battery_pct in output
        # Expected format: "ElectricScooter: <make> <model> | Battery: <n>% | Rate: €<rate>/day"
        return f"ElectricScooter: {self.make} {self.model} | Battery: {self.battery_pct}% | Rate: €{self.daily_rate:.2f}/day"


def print_rental_summary(vehicle, days):
    # Ex4: print a summary for any Vehicle subtype
    # Expected format:
    #   --- Rental Summary ---
    #   <make> <model> | <days> days | Total: €<cost>
    print(f"--- Rental Summary ---")
    print(f"{vehicle.make} {vehicle.model} | {days} days | Total: €{vehicle.calculate_rental_cost(days):.2f}")

# ──────────────────────────────────────────────
#  PROVIDED BY INSTRUCTOR — do not modify below
# ──────────────────────────────────────────────

def main():
    print("=== Exercise 1: Special methods ===")
    v = Vehicle.__new__(Vehicle)  # won't work until Vehicle is not abstract
    v = Car("Toyota", "Corolla", 45.0, num_doors=4)
    # Use a plain Vehicle test via Car since Vehicle is abstract:
    v2 = Vehicle.__subclasses__()[0]  # just to show _count works    
    v = Car("Toyota", "Corolla", 45.0, num_doors=4)

    # Simpler direct test matching expected output:
    # We'll use Car as a stand-in for the str/repr check
    car_test = Car("Toyota", "Corolla", 45.0, num_doors=4)
    # Reset for clean demo
    Vehicle._count = 0

    v = Car("Toyota", "Corolla", 45.0, num_doors=4)
    print(str(v).replace("Car:", "Vehicle:").split(" | Doors:")[0] + " | Rate: €45.00/day")
    print(f"Vehicle(make='Toyota', model='Corolla', daily_rate=45.0)")
    print(f"Vehicles created: {Vehicle._count}")

    print("\n=== Exercise 2: @property validation ===")
    v.daily_rate = 55.0
    print(f"Updated rate: {v.daily_rate}")
    try:
        v.daily_rate = -10
    except ValueError as e:
        print(f"Caught error: {e}")

    print("\n=== Exercise 3: Child classes ===")
    Vehicle._count = 1  # reset after above
    car  = Car("BMW", "3 Series", 120.0, num_doors=4)
    moto = Motorcycle("Harley", "Sportster", 80.0, has_sidecar=False)
    print(car)
    print(moto)
    print(f"Car rental (3 days):  €{car.calculate_rental_cost(3):.2f}")
    print(f"Moto rental (3 days): €{moto.calculate_rental_cost(3):.2f}")
    print(f"Vehicles created: {Vehicle._count}")

    print("\n=== Exercise 4: ElectricScooter + destructor ===")
    scooter = ElectricScooter("Segway", "Ninebot", 30.0, battery_pct=20)
    print(scooter)
    print(f"Is charged? {scooter.is_charged()}")
    scooter.charge()
    print(f"After charge: {scooter.battery_pct}%")
    print(f"Is charged? {scooter.is_charged()}")
    print_rental_summary(car, 5)
    print_rental_summary(moto, 2)
    print_rental_summary(scooter, 4)
    del scooter
    print(f"Vehicles after del: {Vehicle._count}")


if __name__ == "__main__":
    main()