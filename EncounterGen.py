

class EncounterCard:
    def __init__(self):
        self.userInput = ""
    
class NPC:
    def __init__(self):
        self.name = "Rylea"
        self.pospWorldLocations  = ['1','2','3']
        self.pospMapLocaions = ['1','2','3']
        self.pref = ['Fitness, Observation']
        self.dislikes['Research', 'Resolve']
        self.gossipText = ['Did you know I\'m an NPC?']
        

Rylea = NPC()

print(Rylea.name)