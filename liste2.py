homme = ['Jean', 'Rafa', 'Ghania', 'Jeremi', 'Mohammed', 'Ping', 'Geroge']
femme = ['Dana', 'Marina', 'Pauline', 'Fatima', 'kathija', 'Nadine']
#teste vide
def vide(homme):
    if (homme) == []:
        return True
    else:
        return False
#test permiere
def prem(femme):
    if (femme) >= []:
        return femme[0]
    else:
        return False
#test reste
def reste(femme):
    if (femme) >= []:
        return femme[1:]
    else:
        return False
#question 1
def postion(femme):
    if (femme) >= []:
        return femme[2:4]
    else:
        return False
#une liste      
class MyContainer:
    def __contains__(self, value):
        return value is not None   #not none is evry thing 

# cardinal
def card(femme):
    if vide(femme):
        return 0
    else:
        return (1+card(reste(femme)))
#
class mySizeable:
    def __len__(self):
        return 18
    
