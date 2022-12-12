class League:
    def __init__(self, name, nationality, teams, players):
        self.name = name
        self.nationality = nationality
        self.teams = teams
        self.players = players

    def printed(self):
        print(self.name)
        print(f"Národnost - {self.nationality}")
        print("Týmy:")
        for i, teams in enumerate(self.teams):
            print(i+1, teams)
        print("Hráči:")
        for i, players in enumerate(self.players):
            print(i+1, players)

laliga = League("La Liga", "Španělsko", ["Real Madrid", "Barcelona", "Atlético Madrid"], ["Vesi", "Kurf", "Novas", "Chrasťa"])
premierleague = League("Premier League", "Anglie", ["Arsenal", "Chelsea", "Manchester City"], ["Vesi", "Kurf", "Novas", "Chrasťa"])   
premierleague.printed()

