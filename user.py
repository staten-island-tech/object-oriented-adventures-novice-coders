class user:
    def __init__(self, name, health, lvl):
        self.name = name
        self.health = health
        self.lvl = lvl
    def __str__(self):
        return f"{self.name}, {self.health}, {self.lvl}"
    
def player():
    name = input("Enter in a name please: ")
    
