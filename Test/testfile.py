WAY_TO_FILE = "Test/testnames"

while True:
    test = input("Zadej co chceš: ")
    if test == "":
        print("Program ukončen")
        break
    else:
        with open(WAY_TO_FILE, mode='a', encoding="utf-8") as file:
            file.write(test + "\n")
           
def soubor():
    soubor = open(WAY_TO_FILE, mode="r")

    for index, i in enumerate(soubor.readlines()):
        print(str(index + 1) + ". " + i, end="")
    soubor.close()

def list_file():
    with open(WAY_TO_FILE, mode="r") as f:
        f_soubor = f.readlines()
    return f_soubor

def final_file(list_number, list_rename):
    new_list = []
    for index, i in enumerate(list_file()):
        if index + 1 == list_number:
            new_list.append(list_rename + "\n")
        else:
            new_list.append(i)

    return new_list

while True:
    soubor()
    choice = input("Chceš udělat změnu? ano/ne: ")
    if choice == "ne":
        soubor()
        break
    else:
        list = final_file(list_number = int(input("Zadej řádek, který chceš přepsat: ")), list_rename=input("Přepiš řádek: "))
        with open(WAY_TO_FILE, mode='w', encoding="utf-8") as file:
            for index, i in enumerate(list):
                file.write(i)


