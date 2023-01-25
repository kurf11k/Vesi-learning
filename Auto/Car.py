# Cesta k souboru
CAR_PATH = "Auto/file_car"

# Třídy
class Auto:
    def __init__(self, id, značka, počet_sedadel, nádrž, spotřeba):
        self.id = id
        self.značka = značka
        self.počet_sedadel = počet_sedadel
        self.nádrž = nádrž
        self.spotřeba = spotřeba

    def dojezd_na_plnout_nádrž(self):
        x = self.nádrž / self.spotřeba * 100
        x = round(x, 2)
        return x

    def __str__(self):
        return f"{self.id} {self.značka} {self.počet_sedadel} {self.nádrž} {self.spotřeba} {self.dojezd_na_plnout_nádrž()} {self.fix_auto()}"
    


def add_car(car_list):
    id = input("Zadej ID auta: ")
    značka = input("Zadej značku auta: ")
    počet_sedadel = int(input("Zadej počet sedadel: "))
    nádrž = int(input("Zadej objem nádrže v litrech: "))
    spotřeba = float(input("Zadej spotřebu auta: "))
    auto = Auto(id, značka, počet_sedadel, nádrž, spotřeba)
    with open(CAR_PATH, mode="a", encoding="utf-8") as file:
        file.write(auto.id + ";" + auto.značka + ";" + str(auto.počet_sedadel) + ";" + str(auto.nádrž) + ";" + str(auto.spotřeba) + ";" + str(auto.dojezd_na_plnout_nádrž()) + "\n")
    car_list.append(auto)
    return car_list

def update_car(car_id, list):
    new_list = []
    id = input("Zadej ID auta, které chceš opravit: ")
    print("1 - ID")
    print("2 - Značka")
    print("3 - Počet sedadel")
    print("4 - Nádrž")
    print("5 - Spotřeba")
    choice = input("Vyber z nabídky co chceš opravit: ")
    for line in list:
        if line[0] == id and choice == "1":
            choice = input("Zadej nové ID auta: ")
            line = choice, line[1], line[2], line[3], line[4], self.dojezd_na_plnout_nádrž()
            new_list.append(line)
            
        elif line[0] == id and choice == "2":
            choice = input("Zadej novou značku auta: ")
            line = line[0], choice, line[2], line[3], line[4], self.dojezd_na_plnout_nádrž()
            new_list.append(line)

        elif line[0] == id and choice == "3":
            choice = input("Zadej počet sedadel: ")
            line = line[0], line[1], choice, line[3], line[4], self.dojezd_na_plnout_nádrž()
            new_list.append(line)

        elif line[0] == id and choice == "4":
            choice = input("Zadej kapacitu nádrže: ")
            line = line[0], line[1], line[2], choice, line[4], self.dojezd_na_plnout_nádrž()
            new_list.append(line)

        elif line[0] == id and choice == "5":
            choice = input("Zadej spotřebu auta: ")
            line = line[0], line[1], line[2], line[3], choice, self.dojezd_na_plnout_nádrž()
            new_list.append(line)
                
        else:
            new_list.append(line)
    
        with open(CAR_PATH, mode="w") as file:
            for line in list:
                file.write(line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + line[4] + ";" + line[5] + "\n")


def print_seznam_aut():
    file = open(CAR_PATH, mode="r")
    for line in file:
        line = line.split(";")
        print(f"ID: {line[0]}\nZnačka: {line[1]}\nPočet sedadel: {line[2]}\nObjem nádrže: {line[3]}\nSpotřeba: {line[4]}\nDojezd na plnou nádrž: {line[5]}")

def load():
    car_list = []
    with open(CAR_PATH, mode="r") as file:
        for line in file:
            line = line.split(";")
            new_car = Auto(line[0], line[1], line[2], line[3], line[4])
            car_list.append(new_car)
    return car_list

def save(list):
    with open(CAR_PATH, mode="w") as file:
        for line in list:
            file.write(line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + line[4] + ";" + line[5] + "\n")

def smazat_auto(list):
    id = input("Zadej ID auta: ")
    new_list = []
    for line in list:
        if id != line[0]:
            new_list.append(line)

    save(new_list)
    return new_list

car_list = load()

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
        add_car()
    elif choice == "2":
        while True:
            print_seznam_aut()
            print("1 - Opravit parametry auta")
            print("2 - Zpět")
            choice = input("Vyber z nabídky: ")
            if choice == "1":
                list = load()
                Auto.fix_auto()
                continue
            else:
                break
        continue
    elif choice == "3":
        listt = load()
        smazat_auto(listt)
    else:
        break

