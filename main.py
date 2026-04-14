# ──────────────────────────────────────────────
#  VEHICLE RENTAL — CODING CHALLENGE
#  main.py  (provided by instructor, read-only)
#
#  Students: paste this at the bottom of your
#  solution.py file before submitting.
# ──────────────────────────────────────────────
from student_scaffold import Car, Motorcycle, ElectricScooter, Vehicle, print_rental_summary

def main():
    print("=== Exercise 1: Special methods ===")
    v = Car("Toyota", "Corolla", 45.0, num_doors=4)
    print(v)
    print(repr(v))
    print(f"Vehicles created: {Vehicle._count}")

    print("\n=== Exercise 2: @property validation ===")
    v.daily_rate = 55.0
    print(f"Updated rate: {v.daily_rate}")
    try:
        v.daily_rate = -10
    except ValueError as e:
        print(f"Caught error: {e}")

    print("\n=== Exercise 3: Child classes ===")
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