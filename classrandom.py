import random

class Multiply:
    def __init__(self, id, number):
        self.id = id
        self.number = number
    
    def result(self):
        x = self.number * 2
        return x

    def __str__(self):
        return f"{self.id, self.result()}"

def number():   
    x = "123456789"
    number = ""
    for i in range(4):
        i = random.choice(x)
        number += i

    number = int(number)
    return number

def id_object():   
    x = "abcdefghijklmnopqrstuvwxyz123456789"
    object_id = ""
    for i in range(4):
        i = random.choice(x)
        object_id += i
    return object_id

for i in range(10):
    i = Multiply(id_object(), number())
    print(i.number)
