import random

class EncounterCard:
    def __init__(self):
        self.tier = ""
        self.prompt = ""
        self.worldLocation = ""
        self.mapLocation = ""

class pointOfInterest:
    def __init__(self):
        self.mapLocation =""
        self.prompt =""
        self.skillChallenge = ""
    
class npcCard:
    def __init__(self):
        self.name = "Rylea"
        self.pospWorldLocations  = ['1','2','3']
        self.pospMapLocaions = ['1','2','3']
        self.goodPref = ['Fitness', 'Observation']
        self.badPref = ['Fitness', 'Observation']
        self.gossipText = ['Did you know I\'m an NPC?']
        

#def GenerateNpcCard(npcCard):
    #npcCard= ''

ryleaCard = npcCard()


#for x, trait in ryleaCard.__dict__.items():

 #   print(trait)
print(ryleaCard.goodPref[(random.randint(1, 2)-1)])
