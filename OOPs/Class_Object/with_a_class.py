import datetime
class CriketPlayers:
    team_size = 11
    def __init__(self,first_name, last_name, birth_year,team):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.team = team
        self.scores = []
        
    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)
    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year- self.birth_year
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is a player of {self.team} team and was born in {self.birth_year} and has an average score of {self.get_avg_score()}"
    

    
    # below code is for operator overloading, where we are defining the behavior of <, > and == operators for our class objects. In this case, we are comparing the average scores of the players for < operator, ages for > operator and team names for == operator.

    def __lt__(self, other):
        self_avg = self.get_avg_score()
        other_avg = other.get_avg_score()
        return self_avg < other_avg
    
    def __gt__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age > other_age
    
    def __eq__(self, other):
        self_team = self.team
        other_team = other.team
        return self_team == other_team

virat = CriketPlayers('Virat', 'Kohli', 1988, 'India')
virat.add_score(100)
virat.add_score(60)
virat.add_score(80)
print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
print(virat.team)
print(virat.scores)
print(virat.get_avg_score())
print(f"Age of Virat: {virat.get_age()} years")

rohit = CriketPlayers('Rohit', 'Sharma', 1987, 'India')
rohit.add_score(52) 
rohit.add_score(264)
rohit.add_score(150)
print(rohit.first_name)
print(rohit.last_name)
print(rohit.birth_year)
print(rohit.team)
print(rohit.scores)
print(rohit.get_avg_score())
print(f"Age of Rohit: {rohit.get_age()} years")

print(virat)
print(rohit)

print(virat.get_avg_score())
print(rohit.get_avg_score())

# this print are using to understand operator overloading, where we have defined the behavior of <, > and == operators for our class objects.
print(virat < rohit)
print(rohit > virat)
print(virat == rohit)


      
