import random
x1 = random.randint(1,12)
x2 = random.randint(1,12)

def attack():

    answer = int(input("What is the answer? "))
    while answer != x1+x2:
        print("whoops you got it wrong")
        print(x1+x2)
    else: print("yippee you got it")

attack()


""" while monster hp != 0:
	answer = int(input(“What is the answer? “))
	if answer == x1 + x2:
		print(“yippee you got it”)
        monster hp = monster hp - attack dmg
	elif answer != x1 + x2:
print(“whoops you got it wrong”)
else: print(“woohoo you killed the monster”) """