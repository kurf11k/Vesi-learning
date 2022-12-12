number = int(input("Zadej délku straný rovnoramenného trojúhelník "))
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