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
    print("1 - Přidat auto")
    print("2 - Zobrazit auta")
    print("3 - Smazat auto")
    print("4 - Ukončit program")
    choice = input("Vyber z nabídky: ")
    print()
    if choice == "1":
        car_service.add()
        
    elif choice == "2":
        while True:
            car_service.show()
            print("1 - Opravit parametry auta")
            print("2 - Zpět")
            choice = input("Vyber z nabídky: ")
            if choice == "1":
                car_service.update()
            else:
                break
        continue
    elif choice == "3":
        car_service.delete()

    else:
        break

