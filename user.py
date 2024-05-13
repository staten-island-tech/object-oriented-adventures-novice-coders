class user:
    def __init__(self, name, health, lvl, xp):
        self.name = name
        self.health = health
        self.lvl = lvl
        self.xp = xp
    def __str__(self):
        return f"{self.name}, {self.health}, {self.lvl}, {self.xp}"
    name = input("Enter in a name please: ")








"""     def lvl_up(iRange):
        xp = 100
        lvl = 1
        for i in range(iRange):
              if xp == 100:
                    lvl += 1
                    print("You leveled up! Your level is now: " + lvl)   """



