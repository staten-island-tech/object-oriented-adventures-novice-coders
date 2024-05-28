import random
x1 = random.randint(1,12)
x2 = random.randint(1,12)


class attack_types:
    def __init__ (self, name, dealt):
        self.name=name
        self.dealt=dealt

punch=attack_types("punch", 10) #addition
slash=attack_types("slash", 30) #multiplication
push=attack_types("push", 20)   #subtraction
spells=attack_types("spell cast", 40) #Complex equations (combo of 2 operations)

#--------------------------------------------------------
choice=input ("what attack to u want to use? punch, slash, push, spells   ")

def attack():
    if choice == "punch":
        print(str(x1) + " + " + str(x2) + " = ? ")
        answer = int(input("What is the answer? "))
        if answer != x1 + x2:
            print("whoops you got it wrong")
            print("Correct answer: " + str(x1+x2))
        else:
            print("yippee you got it")
            #subtract dmg dealt from monter hp
    elif choice == "slash":
        print(str(x1) + " * " + str(x2) + " = ? ")
        answer = int(input("What is the answer? "))
        if answer != x1 * x2:
            print("whoops you got it wrong")
            print("Correct answer: " + str(x1 * x2))
        else:
            print("yippee you got it")
            #subtract dmg dealt from monter hp
    elif choice == "slash":
        print()

attack()




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