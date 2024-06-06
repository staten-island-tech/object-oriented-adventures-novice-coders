from enemy import totaldmgslime, totaldmgshrub, totaldmggoblin, totaldmgorc, totaldmgDL
from user import players

#place holder health
health = players.health

def slime_attacking():
    attacked= players.health-totaldmgslime #place holder name
    players.health = attacked #place holder
    print ("OH NO YOU'VE BEEN HIT")
    print ("You have: "+ str (attacked) + " HP")

def shrub_attacking():
    attacked=players.health-totaldmgshrub
    players.health = attacked
    print ("OH NO YOU'VE BEEN HIT")
    print ("You have: "+ str (attacked) + " HP")

def goblin_attacking():
    attacked=players.health-totaldmggoblin
    players.health = attacked
    print ("OH NO YOU'VE BEEN HIT")
    print ("You have: "+ str (attacked) + " HP")

def orc_attacking():
    attacked=players.health-totaldmgorc
    players.health = attacked
    print ("OH NO YOU'VE BEEN HIT")
    print ("You have: "+ str (attacked) + " HP")

def DL_attacking():
    attacked=players.health-totaldmgDL
    players.health = attacked
    print ("OH NO YOU'VE BEEN HIT")
    print ("You have: "+ str (attacked) + " HP")

#slime_attacking ()