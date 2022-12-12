print("Seřazení jmen podle abecedy")
x = input("Zadej jména ").title()
new_list = []

def split():
    y = x.split(", ")
    return y

x = split()

def sežazení_podle_abecedy():
    long = len(x)
    while long > 0:
        min = x[0]
        for word in x:
            if word < min:
                min = word
        for i in range(len(x)):
            if min > x[i]:
                min = x[i]
            else:
                první_v_abecede = min
        new_list.append(první_v_abecede)
        x.remove(první_v_abecede)
        long -= 1
    return new_list

def print_list():
    sum = 0
    for i in sežazení_podle_abecedy():
        sum += 1
        print(str(sum) + ". " + i)

print_list()