#basic characteristics 
# notes: THIS DOESN'T INCLUDE WHEN THE ENEMIES ARE ATTACKING USER
#THIS IS ONLY ATTACKING ENEMY AND ATTACKING AGAIN RIGHT AFTER
#RIGHT BEFORE RUNNING ANOTHER ATTACK INCLUDE SOMETHING ABOUT ENEMY ATTACKING USER

from enemy import blobs, shrubs, slimes, goblins, orcs, dungeon_lords
from user import players
class attack_types:
    def __init__ (self, name, dealt):
        self.name=name
        self.dealt=dealt

punch=attack_types("punch", 10)
slash=attack_types("slash", 30)
push=attack_types("push", 20)
spells=attack_types("spell cast", 40)

#--------------------------------------------------------
choice=input ("what attack to u want to use? punch, slash, push, spells   ")
#-------------------------------------------------------------
#BLOB ONLY

def attacking_blob():
    health= blobs.hp
    if choice== "punch":
        res=health-punch.dealt
        blobs.hp=res
        again_blobs ()
    elif choice == "slash":
        res=health-slash.dealt
        blobs.hp=res
        again_blobs ()
    elif choice == "push":
        res=health-push.dealt
        blobs.hp=res
        again_blobs ()
    elif choice == "spells":
        res=health-spells.dealt
        blobs.hp=res
        again_blobs ()
    
def again_blobs():
        if blobs.hp<=0:
            print ("victory")
        else: 
            print ("enemy still has: " + str (blobs.hp))
            choice==input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            attacking_blob()

#-------------------------------------------------------------
#SHURB ONLY

def attacking_shrub():
    health= shrubs.hp
    if choice== "punch":
        res=health-punch.dealt
        shrubs.hp=res
        again_shrubs ()
    elif choice == "slash":
        res=health-slash.dealt
        shrubs.hp=res
        again_shrubs ()
    elif choice == "push":
        res=health-push.dealt
        shrubs.hp=res
        again_shrubs ()
    elif choice == "spells":
        res=health-spells.dealt
        shrubs.hp=res
        again_shrubs ()
    
def again_shrubs():
        if shrubs.hp<=0:
            print ("victory")
            players.xp=players.xp+shrubs.drop
        else: 
            print ("enemy still has: " + str (shrubs.hp))
            choice==input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            attacking_shrub()

#attacking_shrub()
#-------------------------------------------------------
# SLIMES ONLY

def attacking_slime():
    health= slimes.hp
    if choice== "punch":
        res=health-punch.dealt
        slimes.hp=res
        again_slimes ()
    elif choice == "slash":
        res=health-slash.dealt
        slimes.hp=res
        again_slimes ()
    elif choice == "push":
        res=health-push.dealt
        slimes.hp=res
        again_slimes ()
    elif choice == "spells":
        res=health-spells.dealt
        slimes.hp=res
        again_slimes ()
    
def again_slimes():
        if slimes.hp<=0:
            print ("victory")
            players.xp=players.xp+slimes.drop

        else: 
            print ("enemy still has: " + str(slimes.hp))
            choice ==input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            attacking_slime()

#attacking_slime()
#-------------------------------------------------------
# GOBLINS ONLY 

def attacking_goblin():
    health= goblins.hp
    if choice== "punch":
        res=health-punch.dealt
        goblins.hp=res
        again_goblins ()
    elif choice == "slash":
        res=health-slash.dealt
        goblins.hp=res
        again_goblins ()
    elif choice == "push":
        res=health-push.dealt
        goblins.hp=res
        again_goblins ()
    elif choice == "spells":
        res=health-spells.dealt
        goblins.hp=res
        again_goblins ()
    
def again_goblins():
        if goblins.hp<=0:
            print ("victory")
            players.xp=players.xp+goblins.drop
        else: 
            print ("enemy still has: " +str (goblins.hp))
            choice == input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            attacking_goblin()

#attacking_goblin()
#-------------------------------------------------------
# ORCS ONLY 

def attacking_orc():
    health= orcs.hp
    if choice== "punch":
        res=health-(punch.dealt)*.8
        orcs.hp=res
        again_orcs ()
    elif choice == "slash":
        res=health-(slash.dealt)*.8
        orcs.hp=res
        again_orcs ()
    elif choice == "push":
        res=health-(push.dealt)*.8
        orcs.hp=res
        again_orcs ()
    elif choice == "spells":
        res=health-(spells.dealt)*.8
        orcs.hp=res
        again_orcs ()
def again_orcs():
    if orcs.hp<=0:
        print ("victory")
        players.xp=players.xp+orcs.drop
    else: 
        print ("enemy still has: " + str (orcs.hp))
        choice == input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
        attacking_orc()

#attacking_orc()
#-------------------------------------------------------
# DL ONLY

def attacking_dungeon_lord():
    health= dungeon_lords.hp
    if choice== "punch":
        res=health-(punch.dealt)*.8
        dungeon_lords.hp=res
        again_dungeon_lords ()
    elif choice == "slash":
        res=health-(slash.dealt)*.8
        dungeon_lords.hp=res
        again_dungeon_lords ()
    elif choice == "push":
        res=health-(push.dealt)*.8
        dungeon_lords.hp=res
        again_dungeon_lords ()
    elif choice == "spells":
        res=health-(spells.dealt)*.8
        dungeon_lords.hp=res
        again_dungeon_lords ()
def again_dungeon_lords():
    if dungeon_lords.hp<=0:
        print ("victory")
        players.xp=players.xp+dungeon_lords.drop
    else: 
        print ("OH NO, DUNGEON LORD HEALED 5HP")
        boost=dungeon_lords.hp+5
        print ("enemy still has: " + str(boost))
        choice == input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
        attacking_dungeon_lord()

#attacking_dungeon_lord()