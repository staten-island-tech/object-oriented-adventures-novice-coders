from enemy import totaldmgslime, totaldmggoblin, totaldmgorc, totaldmgDL
from player import user 

#doesn't remember the updated hp

#place holder health
health = user.health

def slime_attacking():
    attacked= user.health-totaldmgslime #place holder name
    user.health = attacked #place holder
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

def goblin_attacking():
    attacked=health-totaldmggoblin
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

def orc_attacking():
    attacked=health-totaldmgorc
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

def DL_attacking():
    attacked=health-totaldmgDL
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

slime_attacking ()