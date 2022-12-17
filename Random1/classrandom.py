import random

class Multiply:
    def __init__(self, id, number):
        self.id = id
        self.number = number

    def __str__(self):
        return f"{self.id, self.number}"

def number():   
    x = "123456789"
    number = ""
    for i in range(4):
        i = random.choice(x)
        number += i
    number = int(number)
    number *= 3
    number = str(number)
    return number

def id_object():   
    x = "abcdefghijklmnopqrstuvwxyz123456789"
    object_id = ""
    for i in range(4):
        i = random.choice(x)
        object_id += i
    return object_id

for object in range(10):
    object = Multiply(id_object(), number())
    with open('Random1/random', 'a', encoding="utf-8") as file:
        file.write("ID: " + object.id)
        file.write(" - ")
        file.write("number: " + object.number + "\n")

