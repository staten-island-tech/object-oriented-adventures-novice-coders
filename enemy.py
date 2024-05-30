#Characteristics of each enemy


class shrub:
    def __init__ (self, hp, level, damage, drop):
         self.hp = hp
         self.level = level
         self. damage = damage
         self.drop=drop

class blob:
     def __init__ (self, hp):
          self.hp = hp

class slime (shrub):
     def __init__ (self, hp, level, damage, drop, poison):
          super().__init__(hp, level, damage, drop)
          self.poison = poison
          poison=5
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}"
     
class goblin (slime):
     def __init__ (self, hp, level, damage, drop, poison, double):
          super().__init__(hp, level, damage, drop, poison)
          self.double = double
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}, {self.double}"
     
class orc (goblin):
     def __init__ (self, hp, level, damage, drop , poison, double, less):
          super().__init__(hp, level, damage, drop, poison, double)
          self.less=less
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}, {self.double}, {self.less}"

class dungeon_lord (orc):
     def __init__ (self, hp, level, damage, drop, poison, double, less, heal):
          super().__init__(hp, level, damage, drop, poison, double, less)
          self.heal=heal
     def __str__(self):
          return f"{self.hp}, {self.level}, {self.damage}, {self.poison}, {self.double}, {self.less}, {self.heal}"

#2.0
#format: hp, lvl, dmg, drop, poison, 2x, 20% less hit, heal

blobs= blob (15)
shrubs = shrub (30, 1, 10, 80)
slimes = slime (50, 2, 15, 110, 5)
goblins = goblin (70, 3, 25, 140, 5, 2)
orcs= orc (90, 4, 35, 200, 5, 2, 0.8)
dungeon_lords = dungeon_lord (140, 5, 50, 300, 5, 2, 0.8, 15)


#print (dungeon_lords.heal) #print specific value
#-------------------------------------------------
#calculation of total dmgs below

totaldmgslime=slimes.damage+slimes.poison
#print (totaldmgslime)
#20 dmg

totaldmggoblin=(goblins.damage+goblins.poison)*2
#print (totaldmggoblin)
#60 dmg

totaldmgorc=(orcs.damage+orcs.poison)*2
#print (totaldmgorc)
#80 dmg

totaldmgDL= (dungeon_lords.damage + dungeon_lords.poison)*2
#print (totaldmgDL)
#110 dmg



