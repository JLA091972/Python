from players import players

class Player:
    def __init__(self, data):
        self.name = data['name']
        self. age = data['age']
        self.position = data['position']
        self.team = data['team']

player_objects = []

for player in players:
    player_objects.append(Player(player))