# round()
x = 3842.9915
x = str(x)
y = 2

def lenn(x):
    x = x.split(".")
    return len(x[0])


def integer(x):
    x = float(x)
    return x

def round(y):
    new_str = ""
    sum = 0 
    for i in x:
        if sum == (lenn(x) + 1 + y):
            break
        elif i != ".":
            new_str += i
            sum +=1
    new_str = int(new_str)
    return new_str

def final():
    #for i in range(len(round(y))-2, -1, -1):
    if round(y)[lenn(x) + 1 + y] > 4:
        round(y)[lenn(x) + y] = round(y)[lenn(x) + y] + 1
        round(y)[lenn(x) + 1 + y] = 0
    else:
        round(y)[lenn(x) + 1 + y] = 0
print(final())