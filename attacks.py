#basic characteristics 
from enemy import shrubs, slimes, goblins, orcs, dungeon_lords

class attack_types:
    def __init__ (self, name, dealt):
        self.name=name
        self.dealt=dealt

punch=attack_types("punch", 10)
slash=attack_types("slash", 30)
push=attack_types("push", 20)
spells=attack_types("spell cast", 40)

#-------------------------------------------
# change health to be the enemy health in battle
#figure out how to update health and attack again

""" 
choice=input ("what attack to u want to use? punch, slash, push, spells   ")
health=100
def health_dmg():
    if choice== "punch":
        res=health-punch.dealt
        print (res)
        health.update (res)
    if choice == "slash":
        res=health-slash.dealt
        print (res)
    if choice == "push":
        res=health-push.dealt
        print (res)
    if choice == "spells":
        res=health-spells.dealt
        print (res)

health_dmg()
 """

#--------------------------------------------------------
""" print (health)
again=input ("attack again? Y/N  ")
if again == "Y":
    health_dmg ()
else :
    print ("end")
 """

#-------------------------------------------------------------
#more specific

"""print (shrubs.hp)
print (slimes.hp)"""

choice=input ("what attack to u want to use? punch, slash, push, spells   ")
health= shrubs.hp
def attacking_shrub():
    if choice== "punch":
        res=health-punch.dealt
        shrubs.hp=res
        again ()
    if choice == "slash":
        res=health-slash.dealt
        shrubs.hp=res
        again ()
    if choice == "push":
        res=health-push.dealt
        shrubs.hp=res
        again ()
    if choice == "spells":
        res=health-spells.dealt
        shrubs.hp=res
        again ()
    
def again():
        if shrubs.hp==0:
            print ("victory")
        else: 
            print ("enemy still has: "); print (shrubs.hp)
            choice=input ("what attack to u want to use to attack again? punch, slash, push, spells   ")
            attacking_shrub()

attacking_shrub()
#print (shrubs.hp)
