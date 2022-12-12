x = input("Zadej jména ")
new_list = []

def split():
    y = x.split(" ")
    return y

x = split()

def abeceda():
    long = len(x)
    while long > 0:
        v = x[0]
        for word in x:
            if word < v:
                v = word

            for i in range(len(x)):
                if v > x[i]:
                    v = x[i]
                    první_v_abecede = v
                else:
                    nevím = v

        new_list.append(nevím)
        x.remove(nevím)
        long -= 1
    print(new_list)
abeceda()

