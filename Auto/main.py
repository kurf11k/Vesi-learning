# 1 - read all
# 2 - read one
# 3 - create 
# 4 - update
# 5 - delete

from service import Service
from car import Car

CAR_PATH = "Auto/cars"
car_service = Service(Car, CAR_PATH)


#naimplementuj přidání a smazání ve stejném duchu jako je to s auty
#podívej se jak to funguje a zkus to idělat stejně, tak že vytvoříš novou service
#ta service se bude starat o přídání a smazání planet
#ve zkratce je ta implementace staršně jednoduchá a jsou to cca 4 řádky (v mainu), co musíš napsat, aby to fungovalo
#samozřejmě musíš vytvořit třídu Planet stejným principem jako třídu Car
#ale jde o to, abys pochopil ten princip modulace, že stačí použít něco už hotového a bude to fungovat


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
