class player:
    def __init__(self, name, health, lvl, xp):
        self.name = name
        self.health =health
        self.lvl = lvl
        self.xp = xp
    def __str__(self):
        return f"{self.name}, {self.health}, {self.lvl}, {self.xp}"


#format: name, health, lvl, xp
name=input("Enter in a name please: ")
user=player(name, 500, 1, 0)

print (user.health)




""" health = 300
xp = 0
lvl = 1
#add function for gaining xp after killing monsters, and updating xp value
def lvl_up(self):
    if xp == 100:
        lvl += 1
        print("You leveled up! Your level is now: " + lvl)
        xp = xp - 100
        health = 300

def dead(self):
    health = 300
    if health == 0:
        print("you died")
    



    name = input("Enter in a name please: ")  """