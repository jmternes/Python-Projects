
class Player:
    def player_intro(self):
        print('My name is ' + self.name + ', my height is ' + self.height ' and I play for the ' + self.team)

p1 = Player()
    p1.name = "LeBron"
    p1.height = "6-8"
    p1.team = "Lakers"

p2 = Player()
    p2.name = "Steph"
    p2.height = "6-3"
    p2.team = "Warriors"


p1.player_intro()
p2.player_intro()
