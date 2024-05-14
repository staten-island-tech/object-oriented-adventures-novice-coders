#basic characteristics 
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

choice=input ("what attack to u want to use? punch, slash, push, spells   ")
health=100
def health_dmg():
    if choice== "punch":
        res=health-punch.dealt
        print (res)
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

""" again=input ("attack again? Y/N  ")
if again == "Y":
    health_dmg ()
else :
    print ("end")
 """



