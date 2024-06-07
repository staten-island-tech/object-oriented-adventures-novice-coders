#basic characteristics 
# notes: THIS DOESN'T INCLUDE WHEN THE ENEMIES ARE ATTACKING USER
#THIS IS ONLY ATTACKING ENEMY AND ATTACKING AGAIN RIGHT AFTER
#RIGHT BEFORE RUNNING ANOTHER ATTACK INCLUDE SOMETHING ABOUT ENEMY ATTACKING USER

from enemy import blobs, shrubs, slimes, goblins, orcs, dungeon_lords
from user import players
from enemyATK import shrub_attacking, slime_attacking, goblin_attacking, orc_attacking, DL_attacking
#from equations import equations_shrub
class attack_types:
    def __init__ (self, name, dealt):
        self.name=name
        self.dealt=dealt

punch=attack_types("punch", 10)
slash=attack_types("slash", 30)
push=attack_types("push", 20)
spells=attack_types("spell cast", 40)

#BLOB ONLY

def attacking_blob(choice):
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
            new_choice=input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            equations_blob(new_choice)

#-------------------------------------------------------------
#SHURB ONLY

def attacking_shrub(choice):
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
            shrub_attacking()
            new_choice = input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            equations_shrub (new_choice)

#-------------------------------------------------------
# SLIMES ONLY

def attacking_slime(choice):
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
            slime_attacking()
            new_choice =input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            equations_slime(new_choice)

#-------------------------------------------------------
# GOBLINS ONLY 

def attacking_goblin(choice):
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
            goblin_attacking()
            new_choice = input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            equations_goblin(new_choice)

#-------------------------------------------------------
# ORCS ONLY 

def attacking_orc(choice):
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
        orc_attacking()
        new_choice = input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
        equations_orc(new_choice)

#attacking_orc()
#-------------------------------------------------------
# DL ONLY

def attacking_dungeon_lord(choice):
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
        DL_attacking()
        if players.health>0:
            new_choice = input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            equations_DL(new_choice)

#-------------------------------------------------
def main_blob():
   choice = input ("what attack to u want to use? punch, slash, push, spells   ")
   equations_blob(choice)

def main_shrub():
   choice = input ("what attack to u want to use? punch, slash, push, spells   ")
   equations_shrub(choice)

def main_slime():
   choice = input ("what attack to u want to use? punch, slash, push, spells   ")
   equations_slime(choice)

def main_goblin():
   choice = input ("what attack to u want to use? punch, slash, push, spells   ")
   equations_goblin(choice)

def main_orc():
   choice = input ("what attack to u want to use? punch, slash, push, spells   ")
   equations_orc(choice)

def main_DL():
    choice = input ("what attack to u want to use? punch, slash, push, spells   ")
    equations_DL(choice)
#-------------------------------------------------
import random

"""
x1 = random.randint(1,12)
x2 = random.randint(1,12)
x3 = random.randint(1,12)

"""

#--------------------- equations for blob
def equations_blob(choice):
        x1 = random.randint(1,12)
        x2 = random.randint(1,12)
        x3 = random.randint(1,12)
        if choice == "punch":
            print(str(x1) + " + " + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 + x2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(x1+x2))
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_blob(choice)
        elif choice == "slash":
            print(str(x1) + " * " + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 * x2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(x1 * x2))
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_blob(choice)
        elif choice == "push":
            print(str(x1) + "-" + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 - x2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(x1 - x2))
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_blob(choice)
        elif choice == "spells":
            print(str(x1) + "+" + str(x2) + "*" + str(x3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == x1 + x2 * x3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_blob(choice)
            elif answer != (x1 + x2) * x3 and x1 + x2 * x3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(x1 + x2 * x3))
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(x1 + x2 * x3))

#--------------------- equations for shrubs
def equations_shrub(choice):
        a1 = random.randint(1,12)
        a2 = random.randint(1,12)
        a3 = random.randint(1,12)
        if choice == "punch":
            print(str(a1) + " + " + str(a2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != a1 + a2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(a1+a2))
                shrub_attacking()
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_shrub(choice)
        elif choice == "slash":
            print(str(a1) + " * " + str(a2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != a1 * a2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(a1 * a2))
                shrub_attacking()
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_shrub(choice)
        elif choice == "push":
            print(str(a1) + "-" + str(a2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != a1 - a2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(a1 - a2))
                shrub_attacking()
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_shrub(choice)
        elif choice == "spells":
            print(str(a1) + "+" + str(a2) + "*" + str(a3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == a1 + a2 * a3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_shrub(choice)
            elif answer != (a1 + a2) * a3 and a1 + a2 * a3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(a1 + a2 * a3))
                shrub_attacking()
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(a1 + a2 * a3))
                shrub_attacking()

#--------------------- equaions for slimes
def equations_slime(choice):
        b1 = random.randint(1,12)
        b2 = random.randint(1,12)
        b3 = random.randint(1,12)
        if choice == "punch":
            print(str(b1) + " + " + str(b2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != b1 + b2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(b1+b2))
                slime_attacking()
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_slime(choice)
        elif choice == "slash":
            print(str(b1) + " * " + str(b2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != b1 * b2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(b1 * b2))
                slime_attacking()
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_slime(choice)
        elif choice == "push":
            print(str(b1) + "-" + str(b2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != b1 - b2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(b1 - b2))
                slime_attacking()
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_slime(choice)
        elif choice == "spells":
            print(str(b1) + "+" + str(b2) + "*" + str(b3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == b1 + b2 * b3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_slime(choice)
            elif answer != (b1 + b2) * b3 and b1 + b2 * b3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(b1 + b2 * b3))
                slime_attacking()
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(b1 + b2 * b3))
                slime_attacking()

#--------------------- equations for goblins
def equations_goblin(choice):
        c1 = random.randint(1,12)
        c2 = random.randint(1,12)
        c3 = random.randint(1,12)
        if choice == "punch":
            print(str(c1) + " + " + str(c2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != c1 + c2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(c1+c2))
                goblin_attacking()
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_goblin(choice)
        elif choice == "slash":
            print(str(c1) + " * " + str(c2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != c1 * c2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(c1 * c2))
                goblin_attacking()
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_goblin(choice)
        elif choice == "push":
            print(str(c1) + "-" + str(c2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != c1 - c2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(c1 - c2))
                goblin_attacking()
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_goblin(choice)
        elif choice == "spells":
            print(str(c1) + "+" + str(c2) + "*" + str(c3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == c1 + c2 * c3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_goblin(choice)
            elif answer != (c1 + c2) * c3 and c1 + c2 * c3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(c1 + c2 * c3))
                goblin_attacking()
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(c1 + c2 * c3))
                goblin_attacking()

#--------------------- equations for orcs
def equations_orc(choice):
        d1 = random.randint(1,12)
        d2 = random.randint(1,12)
        d3 = random.randint(1,12)
        if choice == "punch":
            print(str(d1) + " + " + str(d2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != d1 + d2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(d1+d2))
                orc_attacking()
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_orc(choice)
        elif choice == "slash":
            print(str(d1) + " * " + str(d2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != d1 * d2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(d1 * d2))
                orc_attacking()
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_orc(choice)
        elif choice == "push":
            print(str(d1) + "-" + str(d2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != d1 - d2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(d1 - d2))
                orc_attacking()
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_orc(choice)
        elif choice == "spells":
            print(str(d1) + "+" + str(d2) + "*" + str(d3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == d1 + d2 * d3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_orc(choice)
            elif answer != (d1 + d2) * d3 and d1 + d2 * d3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(d1 + d2 * d3))
                orc_attacking()
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(d1 + d2 * d3))
                orc_attacking()

#--------------------- equations for DL
def equations_DL(choice):
        e1 = random.randint(1,12)
        e2 = random.randint(1,12)
        e3 = random.randint(1,12)
        if choice == "punch":
            print(str(e1) + " + " + str(e2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != e1 + e2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(e1+e2))
                DL_attacking()
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
                attacking_dungeon_lord(choice)
        elif choice == "slash":
            print(str(e1) + " * " + str(e2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != e1 * e2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(e1 * e2))
                DL_attacking()
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
                attacking_dungeon_lord(choice)
        elif choice == "push":
            print(str(e1) + "-" + str(e2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != e1 - e2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(e1 - e2))
                DL_attacking()
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
                attacking_dungeon_lord(choice)
        elif choice == "spells":
            print(str(e1) + "+" + str(e2) + "*" + str(e3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == e1 + e2 * e3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
                attacking_dungeon_lord(choice)
            elif answer != (e1 + e2) * e3 and e1 + e2 * e3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(e1 + e2 * e3))
                DL_attacking()
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(e1 + e2 * e3))
                DL_attacking()