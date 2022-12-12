class Father:
    def __init__(self, eyes, head, body):
        self.eyes = eyes
        self.head = head
        self.body = body
        #print(f"{self.eyes}, {self.head}, {self.body}")
        
class Mother(Father):
    def __init__(self, eyes, head, body, hand, legs, hair):
        super().__init__(eyes, head, body)
        self.hand = hand
        self.legs = legs
        self.hair = hair

class Me(Mother):
    def __init__(self, name, lastname, eyes, head, body, hand, legs, hair):
        self.name = name
        self.lastname =lastname
        super().__init__(eyes, head, body, hand, legs, hair)

    def __str__(self): 
        return f"{self.name} {self.lastname} {self.eyes} {self.head} {self.body} {self.hand} {self.legs} {self.hair}"

#me = Me(1, 2, 3)
x = Me("1", "2", "3", "4", "5", "6", "7", "8")
print()