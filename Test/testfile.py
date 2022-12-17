while True:
    test = input("Zadej co chceš: ")
    if test == "":
        print("Program ukončen")
        break
    else:
        with open('Test/testnames', 'a', encoding="utf-8") as file:
            file.write(test)
