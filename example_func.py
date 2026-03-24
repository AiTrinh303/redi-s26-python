def get_name():
    name = input("Enter your name: ")
    return name  

def get_home_town():
    home_town = input("Enter your hometown: ")
    return home_town        

username = get_name()
hometown = get_home_town()


def greet_user(name, home):
    print(f"Hello, {name}! You are from {home}.")

   
# def greet_user():
#     name = get_name()
#     home = get_home_town()
#     print(f"Hello, {name}! You are from {home}.")


# greet_user()        



# greet_user(name=username, home=hometown)    

# greet_user(name=get_name(), home=get_home_town())


# def avg_temp ( *args: float ) -> float:
#     total = 0.0
#     for arg in args:
#         total += arg
#     return total / len(args)

# print(avg_temp(70.0, 75.0, 80.0))

# def configure_laptop(**kwargs: dict):
#     print(type(kwargs))
#     print(f"\nConfiguring a laptop with the following specifications:\n")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# configure_laptop(brand="Dell", processor="Intel i7", ram="16GB", storage="512GB SSD")    

# configure_laptop(brand="Apple", processor="M1", ram="16GB", storage="1TB SSD", color="Space Gray")

# def func(a, /, b, c=100,*pc,d, **kwargs):
#     print(f"a: {a}, b: {b}, c: {c}, pc: {pc}, d: {d}, kwargs: {kwargs}")

# func(1, 2, 3, 4, 5, d=6, e=7, f=8)