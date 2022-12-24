NAMES_PATH = "Test/testnames"

def add_name():
    test = input("Zadej jméno: ")
    with open(NAMES_PATH, mode='a', encoding="utf-8") as file:
        file.write(test + "\n")
           
def list_names():
    soubor = open(NAMES_PATH, mode="r")

    for index, i in enumerate(soubor.readlines()):
        print(str(index + 1) + ". " + i, end="")
    soubor.close()

def list_file():
    with open(NAMES_PATH, mode="r") as f:
        f_soubor = f.readlines()
    return f_soubor

def list_for_rewrite(list_number, list_rename):
    new_list = []
    for index, i in enumerate(list_file()):
        if index + 1 == list_number:
            new_list.append(list_rename + "\n")
        else:
            new_list.append(i)
    return new_list

def rewrite():
    list = list_for_rewrite(list_number = int(input("Zadej řádek, který chceš přepsat: ")), list_rename=input("Přepiš řádek: "))
    with open(NAMES_PATH, mode='w', encoding="utf-8") as file:
        for i in list:
            file.write(i)


def list_for_delete_name(list_number):
    new_list = []
    for index, i in enumerate(list_file()):
        if index + 1 == list_number:
            continue
        else:
            new_list.append(i)
    return new_list

def delete_name():
    list = list_for_delete_name(list_number=int(input("Zadej řádek, který chceš smazat: ")))
    with open(NAMES_PATH, mode="w", encoding="utf-8") as file:
        for i in list:
            file.write(i)

# main loop
while True:
    print("MENU")
    print("0 - Seznam jmen")
    print("1 - Přidat jméno")
    print("2 - Změnit jméno")
    print("3 - Smazat jméno")
    print("4 - Ukončit")
    choice = input("Vyber z možnosti: ")
    if choice == "0":
        list_names()
        input("Zpět ")
        continue

    elif choice == "1":
        add_name()
        continue
        
    elif choice == "2":
        list_names()
        rewrite()
        continue

    elif choice == "3":
        list_names()
        delete_name()
        continue

    elif choice == "4":
        print("Ukončit program")
        break
    
    else:
        input("Chyba zkus to znova ")
        continue

