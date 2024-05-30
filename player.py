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


def lvl_up ():
    if user.xp>=100:
        up=user.lvl+1
        print ("you lvled up to: "+ str (up))
        user.xp=user.xp-100
        user.health=500

#lvl_up()

def dead():
    if user.health == 0:
        print("you died")

