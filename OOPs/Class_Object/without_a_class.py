import datetime
def get_avg_score(player):
    return sum(player['scores'])/len(player['scores'])


def get_age(player):
    current_year = datetime.datetime.now().year
    return current_year- player['birth_year']

virat={
'first':'Virat',
'last':'Kohli',
'scores': [],
'birth_year': 1988

}
rohit={
'first':'ROhit',
'last':'Sharma',
'scores': [],
'birth_year': 1987

}

virat['scores'].append(100)
virat['scores'].append(60)

rohit['scores'].append(52)
rohit['scores'].append(264)

print(get_avg_score(virat))
print(get_age(virat))

print(get_avg_score(rohit))
print(get_age(rohit))