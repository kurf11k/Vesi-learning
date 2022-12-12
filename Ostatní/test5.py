def obdelník(strana_A, strana_B):
    for i in range(strana_A):
        print(end="* ")
    print("")

    for j in range(1 ,strana_B - 1):
        print("* ", "  " * (strana_A - 3), "*")

    for k in range(strana_A):
        print(end="* ")


def trojúhelník(number):
    if number == 1:
        print("+")
    else:
        number -= 2
        print(" " * number + " +")
        for i in range(number):
            for j in range(number, i, -1):
                print(end=" ")
            print("+ " + i * "  " + "+")
        print("+ " * (number + 2))


while True:    
    x = int(input("Zadej číslo 1 pro obdelník nebo číslo 2 pro trojúhelník "))
    if x == 1: 
        obdelník(strana_A=int(input("Zadej délku strany A ")),strana_B=int(input("Zadej délku strany B ")))
        break
    elif x == 2:
        trojúhelník(number = int(input("\nZadej délku straný rovnoramenného trojúhelník ")))
        break
    else:
        print("Chyba! Zkus to znova")
