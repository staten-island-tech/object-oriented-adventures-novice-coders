class user:
    def __init__(self, name, health, lvl, xp):
        self.name = name
        self.health = health
        self.lvl = lvl
        self.xp = xp
    def __str__(self):
        return f"{self.name}, {self.health}, {self.lvl}, {self.xp}"
    name = input("Enter in a name please: ")

