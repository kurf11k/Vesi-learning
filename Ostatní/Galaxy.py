class Galaxy:
    def __init__(self, name):
        self.name = name
        self.planets = []

    def add_planet(self, name):
        planet = Planet(name)
        self.planets.append(planet)
        return planet
    
    def show(self):
        return f"{self.name} {self.planets}"

class Planet:
    def __init__(self, name):
        self.name = name
        self.states = []

    def add_state(self, name):
        state = State(name)
        self.states.append(state)
        return state

    def __str__(self):
        return f"{self.name}"

class State:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


galaxy1 = Galaxy("Dark")
galaxy1.add_planet("Jupiter")
state = State("Italy")

print(galaxy1.show())

