new_list = [1, 2, 3, 4, 5, 6]
def math(number):
    list = []
    sum = 1
    for i in new_list:
        if sum == number:
            continue
        else:   
            list.append(i)
    print(list)

math(number=int(input("Zadej ")))
