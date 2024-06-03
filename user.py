class player:
    def __init__(self, name, health, lvl, xp):
        self.name = name
        self.health = int(health)
        self.lvl = int(lvl)
        self.xp = int(xp)
    def __str__(self):
        return f"{self.name}, {self.health}, {self.lvl}, {self.xp}"
    

    health = 500
    xp = 0
    lvl = 1
    #add function for gaining xp after killing monsters, and updating xp value
    def lvl_up(self):
        if xp >= 100:
             lvl += 1
             print("You leveled up! Your level is now: " + str(lvl))
             xp = xp - 100
             health = 500
    def dead(self):
        health = 500
        if health == 0:
            print("you died")


name = input("Enter in a name please: ")
players = player(name, 500, 1, 0)



