from enemy import totaldmgslime, totaldmggoblin, totaldmgorc, totaldmgDL
from player import user 
from user import players

#doesn't remember the updated hp

#place holder health
health = players.health

def slime_attacking():
    attacked= players.health-totaldmgslime #place holder name
    players.health = attacked #place holder
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

def goblin_attacking():
    attacked=players.health-totaldmggoblin
    players.health = attacked
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

def orc_attacking():
    attacked=players.health-totaldmgorc
    players.health = attacked
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

def DL_attacking():
    attacked=players.health-totaldmgDL
    players.health = attacked
    print ("you've been attacked")
    print ("You have: "+ str (attacked) + " HP")

#slime_attacking ()