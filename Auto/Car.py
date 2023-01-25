class Car:
    def __init__(self, id=None, brand=None, model=None, count_seats=None):
        self.id = id
        self.brand = brand
        self.model = model
        self.count_seats = count_seats
    
    def load_from_file(self, props):
        self.id = props[0]
        self.brand = props[1]
        self.model = props[2]
        self.count_seats = props[3]
    
    def to_save(self):
        return f"{self.id};{self.brand};{self.model};{self.count_seats}"

    def __str__(self):
        return f"{self.id} {self.brand}"

