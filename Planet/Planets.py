class Planet:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.state = []

    def add_state(self, new_state):
        self.state.append(new_state)

        file = open(CITY_PATH, mode="a", encoding='utf-8')
        file.write(f"{new_state.id};{new_state.name}\n")
        file.close()


class State:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.city = []

    def add_city(self, new_city):
        self.city.append(new_city)

        file = open(CITY_PATH, mode="a", encoding='utf-8')
        file.write(f"{new_city.id};{new_city.name}\n")
        file.close() 

class City:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.id} {self.name}"

STATE_PATH = "Planets/State"
CITY_PATH = "Planets/City"

# Funkce

def load_state():
    states = []
    file = open(file=STATE_PATH, mode="r", encoding="utf-8")
    for line in file:
        list_state = line.split(";")
        new_state = State(list_state[0], list_state[1].replace("\n", ""))
        states.append(new_state)
        return states

def load_city(states):
    file = open(file=CITY_PATH, mode="r", encoding="utf-8")
    for line in file:
        list_city = line.split(";")
        new_city = City(int(list_city[0], list_city[1]))
        for state in states:
            if state.id == list_city[0]:
                state.city.append(new_city)



state = load_state()
load_city(state)

for i in state:
    print(i.id)