import random
from attacks import attacking_shrub

x1 = random.randint(1,12)
x2 = random.randint(1,12)
x3 = random.randint(1,12)


class attack_types:
    def __init__ (self, name, dealt):
        self.name=name
        self.dealt=dealt

punch=attack_types("punch", 10) #addition
slash=attack_types("slash", 30) #multiplication
push=attack_types("push", 20)   #subtraction
spells=attack_types("spell cast", 40) #Complex equations (combo of 2 operations)

#--------------------------------------------------------
'''
def equations():
    while shrubs.hp, blobs.hp, slimes.hp, goblins.hp, orcs.hp, dungeon_lords.hp != 0:
        choice=input ("what attack to u want to use? punch, slash, push, spells   ")
        if choice == "punch":
            print(str(x1) + " + " + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 + x2:
                print("You try to punch your opponent, only to miss your swing and stumble, giving the monster the opportunity to attack. You just failed to do kindergarten math :/")
                print("Correct answer: " + str(x1+x2))
            else:
                print("Congratulations you can do basic math; you bring your arm back and drive it straight into the monster's gut, as it howls in pain.")
        elif choice == "slash":
            print(str(x1) + " * " + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 * x2:
                print("You pull your rusty dagger you found on the side of a street and bring it in a downward slash, but your grip on the weapon wasn't strong enough, and it slips before you can even hit your opponent. Looks like you need to work on your skills, in math and combat")
                print("Correct answer: " + str(x1 * x2))
            else:
                print("Yay you can multiply; using your blade, you swiftly drag it down the monster's back, doing a decent amount of damage.")
        elif choice == "push":
            print(str(x1) + "-" + str(x2) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer != x1 - x2:
                print("Really? :/ I hope you know the monster is probably laughing at your terrible skill. Deciding to just wing it, you bring your arms out and rush forward to push your enemy back, but the universe seems to hate you as you somehow manage to trip on nothing and fall flat on your face in front of the monster as it prepares to retaliate.")
                print("Correct answer: " + str(x1 - x2))
            else:
                print("Good to know you can at least subtract; an intrusive thought enters your head and before you know it, you have tackled the monster and pushed it back knocking it against the wall and giving it quite the concussion, if monsters can get concussions.")
        elif choice == "spells":
            print(str(x1) + "+" + str(x2) + "*" + str(x3) + " = ? ")
            answer = int(input("What is the answer? (Warning: failure to attack results in no damage dealt, solve the problem correctly to attack successfully) "))
            if answer == x1 + x2 * x3:
                print("You mutter some mumbo-jumbo from memory that you've heard that one crazy hobo wizard chant in his hut, and miraculously, it seems to do something as the monster stops,looking confused, and suddenly hits itself with an incredible amount of force. yayy you solved a multi-operation problem :D")
            elif answer != (x1 + x2) * x3 and x1 + x2 * x3:
                print("Good effort, but no, it is not " + str(answer) + ". A traveling witch once taught you a spell to launch your foes several feet away from you, quite useful in this moment where the monster was approaching you in a threatening manner. You quickly draw your wand and yell out the spell, but uh-oh. It seems you should have practiced more, as nothing happens, and the monster appears even more irritated at your foolish antics.")
                print("Correct answer: " + str(x1 + x2 * x3))
            else:
                print("You remember snooping through your mother's magic scrolls and finding a powerful spell that shoots lightning at your target, you quickly mutter the incantation, yet nothing happened. Oh no! You forgot to draw your wand first, like how does one even forget the order of things? (bruh imagine forgetting PEMDAS)")
                print("Correct answer: " + str(x1 + x2 * x3))
    else:
        print("Woohoo the monster died")

equations()




#test
""" def PEMDAS():
    print(str(x1) + "+" + str(x2) + "*" + str(x3) + " = ? ")
    answer = int(input("What is the answer? "))
    if answer == x1 + x2 * x3:
        print("yippee you got it")
    elif answer != (x1 + x2) * x3 and x1 + x2 * x3:
        print("whoops you got it wrong")
        print("Correct answer: " + str(x1 + x2 * x3))
    else:
        print("bruh imagine forgetting PEMDAS")
        print("Correct answer: " + str(x1 + x2 * x3))

PEMDAS() """

#alternative
""" while monster hp != 0:
    print(str(x1) + " + " + str(x2) + " = ? ")
	answer = int(input(“What is the answer? “))
	if answer == x1 + x2:
		print(“yippee you got it”)
        monster hp = monster hp - attack dmg
	elif answer != x1 + x2:
        print(“whoops you got it wrong”)
        print(x1+x2)
else: print(“woohoo you killed the monster”)  """

#--------------------------------------------------------

def equations_shrub():
    #while shrubs.hp, blobs.hp, slimes.hp, goblins.hp, orcs.hp, dungeon_lords.hp != 0:
        choice=input ("what attack to u want to use? punch, slash, push, spells   ")
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
    #else:
        #print("Woohoo the monster died")
                
equations_shrub()
'''