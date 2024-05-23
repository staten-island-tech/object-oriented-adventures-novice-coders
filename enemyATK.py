from enemy import totaldmgslime, totaldmggoblin, totaldmgorc, totaldmgDL
from player import user 

#doesn't remember the updated hp

#place holder health
health = user.health

def slime_attacking():
    attacked= health-totaldmgslime
    health = attacked
    print ("you've been attacked")
    print ("You have:")
    print (attacked)
    again ()

def again():
    miss=("did you miss? Y/N")
    if miss =="Y":
        print ("oh no, you were attacked again")
        slime_attacking()


def goblin_attacking():
    attacked=health-totaldmggoblin
    print ("you've been attacked")
    print ("You have:")
    print (attacked)

def orc_attacking():
    attacked=health-totaldmgorc
    print ("you've been attacked")
    print ("You have:")
    print (attacked)

def DL_attacking():
    attacked=health-totaldmgDL
    print ("you've been attacked")
    print ("You have:")
    print (attacked)

slime_attacking ()