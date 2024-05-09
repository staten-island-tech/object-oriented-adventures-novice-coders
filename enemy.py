class shrub:
    def __init__ (self, hp, level, damage):
         self.hp = hp
         self.level = level
         self. damage = damage

class slime (shrub):
     def __init__ (self, hp, level, damage, poison):
          super().__init__(hp, level, damage)
          self.poison=poison
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}"
     
class goblin (slime):
     def __init__ (self, hp, level, damage, poison, double):
          super().__init__(hp, level, damage, poison)
          self.double = double
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}, {self.double}"
     
class orc (goblin):
     def __init__ (self, hp, level, damage, poison, double, less):
          super().__init__(hp, level, damage, poison, double)
          self.less=less
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}, {self.double}, {self.less}"

class dungeon_lord (orc):
     def __init__ (self, hp, level, damage, poison, double, less, heal):
          super().__init__(hp, level, damage, poison, double, less)
          self.heal=heal
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}, {self.double}, {self.less}, {self.heal}"


shrubs = shrub ("30HP", "Level 1", "10 damage")
slimes =  slime ("50HP", "Level 2", "15 damage", "5 additional damage")
goblins = goblin ("70HP", "Level 3", "25 damage", "5 additional damage", ) 
orcs=  orc ("90HP", "Level 4", "35 damagae")
dungeon_lords = dungeon_lord ("140HP", "Level 5", "50 damage")
