import datetime

class Player:
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    def get_age(self):
        now = datetime.datetime.now().year
        return now - self.birth_year


class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year):
        super().__init__(fname, lname, birth_year)
        self.aces = []

    def get_average_aces_per_match(self):
        return sum(self.aces) / len(self.aces)


class CricketPlayers(Player):
    def __init__(self, fname, lname, team, birth_year):  
      # Player.__init__(self, fname, lname, birth_year)
      # or we can use super() function to call the parent class constructor
        super().__init__(fname, lname, birth_year)
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def add_avg_score(self):
        return sum(self.scores) / len(self.scores)


virat = CricketPlayers('Virat', 'Kohli', 'India', 1988)
virat.add_score(100)
virat.add_score(60)
virat.add_score(80)

print("Age of Virat:", virat.get_age())
print("Average score of Virat:", virat.add_avg_score())

roger = TennisPlayer("Roger", "Federer", 1981)
print(roger.first_name)

