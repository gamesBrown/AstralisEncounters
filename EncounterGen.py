import random

class EncounterCard:
    def __init__(self):
        self.userInput = ""
    
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
print 