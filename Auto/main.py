from car import Car
import storage

CAR_PATH = "Auto/cars"

# 1 - read all
# 2 - read one
# 3 - create 
# 4 - update
# 5 - delete

def show(list):
    for obj in list:
        print(obj)

cars = storage.load(Car, CAR_PATH, ";")
show(cars)
