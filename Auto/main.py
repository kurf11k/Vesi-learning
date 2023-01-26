# 1 - read all
# 2 - read one
# 3 - create 
# 4 - update
# 5 - delete

from service import Service
from car import Car

CAR_PATH = "Auto/cars"
car_service = Service(Car, CAR_PATH)

# Hlavní cyklus
while True:
    print("MENU")
    print("1 - Cars")
    print("2 - Planets")
    print("0 - End")

    choice = input("Type choice: ")

    if choice == "1":
        car_service.show_menu()
        
    elif choice == "2":
        # tady bude planet_service.show_menu()
        pass
    
    else:
        break
