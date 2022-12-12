class Request:
    def __init__(self, player, request_team):
        self.player = player
        self.request_team = request_team

class Player:
    def __init__(self, _name, _lastname, _age, _jersey_number, team):
        self.name = _name
        self.lastname = _lastname
        self.age = _age
        self.jersey_number = _jersey_number
        self.team = team
        
    def request_for_transfer(self, request_team):  
        request = Request(self, request_team)
        self.team.requests.append(request)
        print(f"Zažádáno o přestup do {request_team.name}")
        
    def show(self):
        print(f"{self.name} {self.lastname} je hráčem {self.team.name}")


class Team:
    def __init__(self, name, league):
        self.name = name
        self.league = league
        self.players = []
        self.requests = []
        
    def add_player(self, name, lastname, age, jersey_number):
        new_player = Player(name, lastname, age, jersey_number, self)
        self.players.append(new_player)
        return new_player  
        
    def confirm_transfer(self, player):
        for req in self.requests:
            if req.player == player:
                self.players.remove(player)
                req.request_team.players.append(player)          
                player.team = req.request_team
                print(f"Přestup z {self.name} do {req.request_team.name} byl potvrzen.")
                self.requests.remove(req)
                break
    
    def show(self):
        print(f"Hráči týmu {self.name}:")
        for player in self.players:
            print(f"{player.name} {player.lastname}")            

class League:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.teams = []
        
    def add_team(self, name):
        new_team = Team(name, self)
        self.teams.append(new_team)
        return new_team
        
        
        
premier_league = League("Premier league", "Anglie")

city = premier_league.add_team("Manchester City")
pepa = city.add_player("Pepa", "Jaryn", 5, 19)
honza = city.add_player("Honza", "Jaryn", 6, 19)


arsenal = premier_league.add_team("Arsenal")



pepa.show()
pepa.request_for_transfer(arsenal)
pepa.show()

city.confirm_transfer(pepa)
pepa.show()



