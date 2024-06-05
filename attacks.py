#basic characteristics 
# notes: THIS DOESN'T INCLUDE WHEN THE ENEMIES ARE ATTACKING USER
#THIS IS ONLY ATTACKING ENEMY AND ATTACKING AGAIN RIGHT AFTER
#RIGHT BEFORE RUNNING ANOTHER ATTACK INCLUDE SOMETHING ABOUT ENEMY ATTACKING USER

from enemy import blobs, shrubs, slimes, goblins, orcs, dungeon_lords
from user import players
#from equations import equations_shrub
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
            equations_shrub ()

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
            #attacking_goblin()

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


#-------------------------------------------------
import random


x1 = random.randint(1,12)
x2 = random.randint(1,12)
x3 = random.randint(1,12)


def equations_shrub():
    #while shrubs.hp, blobs.hp, slimes.hp, goblins.hp, orcs.hp, dungeon_lords.hp != 0:

        if choice == "punch":
            print(str(x1) + " + " + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 + x2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(x1+x2))
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_shrub()
        elif choice == "slash":
            print(str(x1) + " * " + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 * x2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(x1 * x2))
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_shrub()
        elif choice == "push":
            print(str(x1) + "-" + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 - x2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(x1 - x2))
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_shrub()
        elif choice == "spells":
            print(str(x1) + "+" + str(x2) + "*" + str(x3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == x1 + x2 * x3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_shrub()
            elif answer != (x1 + x2) * x3 and x1 + x2 * x3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(x1 + x2 * x3))
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(x1 + x2 * x3))

#equations_shrub ()

#choice=input ("what attack to u want to use? punch, slash, push, spells   ")
#attacking_shrub()