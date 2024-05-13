#Characteristics of each enemy (NOT INCLUDING UPDATING HP PER ATTACK)

class shrub:
    def __init__ (self, hp, level, damage):
         self.hp = hp
         self.level = level
         self. damage = damage

class slime (shrub):
     def __init__ (self, hp, level, damage, poison):
          super().__init__(hp, level, damage)
          self.poison = poison
          poison=5
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

#2.0
#format: hp, lvl, dmg, poison, 2x, 20% less hit, heal

shrubs = shrub (30, 1, 10)
slimes = slime (50, 2, 15, 5)
goblins = goblin (70, 3, 25, 5, 2)
orcs= orc (90, 4, 35, 5, 2, 0.8)
dungeon_lords = dungeon_lord (140, 5, 50, 5, 2, 0.8, 15)

#print (dungeon_lords.heal) #print specific value
"""totaldmgDL= (dungeon_lords.damage + dungeon_lords.poison)*2
print (totaldmgDL)"""
#find total of some factor

