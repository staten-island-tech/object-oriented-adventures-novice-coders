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