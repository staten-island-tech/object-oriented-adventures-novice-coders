from enemy import totaldmgslime, totaldmggoblin, totaldmgorc, totaldmgDL

health=500

def slime_attacking():
    attacked= health-totaldmgslime
    health =attacked
    print ("you've been attacked")
    print ("You have:")
    print (attacked)
    slime_attacking ()

def again_attcked():
        print ("youve been attacked again")
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