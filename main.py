from user import players
from enemy import blobs, shrubs, slimes, orcs, goblins, dungeon_lords, totaldmgshrub, totaldmgslime, totaldmgorc, totaldmggoblin, totaldmgDL
from enemyATK import shrub_attacking, slime_attacking, goblin_attacking, orc_attacking, DL_attacking
from attacks import main_blob, main_shrub, main_slime, main_goblin, main_orc, main_DL



def lvl_up():
    if players.xp >= 100:
             players.lvl += 1
             print("You leveled up! Your level is now: " + str(players.lvl))
             players.xp = players.xp - 100
             players.health = 500
             print ("You have: ", players.health, " HP")

def dead():
    if players.health == 0:
        print("you died")
        print ("LETS START OVER >:) ")

def game():

    def start():
        print("Welcome to Your Average Adventure Game! You were kicked out of the hut by your mother to earn some money to support the family, now you have to venture out the village and into the dungeon to fight monsters for gold!")
        print("Here are your current stats; name: " + players.name + ", health: " + str(players.health) + ", xp: " + str(players.xp) + ", lvl: " + str(players.lvl))
        begin = input("Continue? Y/N  ")
        print(begin)
        if begin == "Y" or "y":
            print("Awesome! Let's begin :D")
        elif begin == "N" or "n":
            print("Too bad, you don't have a choice :)")
        else: 
            print("That's not an answer, try again")
            print(begin)

    start()
    print()
    print()
    print ("Instructions: press ENTER to contiue the storyline!")
    print()
    print()

    #NPC MOB
    print ("Mob: Hi", players.name, "How are you on this fine?" )
    input ()
    print ("Mob: Oh, your mother kicked you out!? Jeez, thats rough buddy.")
    input ()
    print ("Mob: Well, there is a blob up ahead in your path. Those are pretty easy to deal with, even a child could take one down.")
    input ()
    print ("Mob: Watch out for Dungeon Lord though! There's been one lurking nearby.")
    input ()
    print ("Mob: I heard its fangs are really valuable, but many adventurers have already been lured by the money only to die by its hands.")
    input ()
    print ("Mob: Good luck out there!")
    input ()

    #COMING TO THE BLOB - intro to instructions
    print()
    print()
    print ("As you began to follow the path, you see something ahead. Its the blob that Mob was talking about!")
    print ("Prepare for battle", players.name, "!")
    print()
    print()
    print ("In this game there are various attacks you can use including: punch, push, slash, and spells")
    print ("Each of these deals a different amount of damage...")
    input()
    print ("punch: 10, push: 20, slash: 30, spells: 40")
    input ()
    print ("But wait, you need to solve simple problem in order to attack your enemy.")
    print ("Incorrectly solving it will do NO DAMAGE to the enemy")
    print ()

    #Blob battle
    print ("your enemy has: ", blobs.hp , "HP")
    def battle_with_blob():
        main_blob()

    battle_with_blob()

    #going into shrub encounter
    print ("HURRAY!!!! You did it!")
    input()
    print ("Its not over yet, let continue moving through this pathway!")
    input ()
    print ("As you begin to journey through the dungeon you began to feel something off about your surroundings")
    input()
    print ("....")
    input ()
    print ("WATCH OUT, ITS THE SHRUB!!!")
    print ()

    #shrub battle
    print ("your enemy has: ", shrubs.hp)
    print ("shrubs do a total damage of:", totaldmgshrub)
    def battle_with_shrub ():
        while shrubs.hp > 0 and players.health>0:
            main_shrub()
        dead()
        print ("HURRAY! Lets keep moving before more come")

    battle_with_shrub()

    #going into slime encounter 
    print()
    print("as you were running through the pathway, the path ahead of you slowly became darker and darker")
    input()
    print ("it slowly became harder and harder to navigate the pathway")
    input()
    print ("it was like you were slowly becoming glued to the ground....")
    input()
    print("as you grab your flash light and turn it on you became horrified my the view below you")
    input()
    print ("It was slimes.....")
    print()

    #slime battle
    print("Your enemy has:", slimes.hp)
    print ("slimes deal a total damage of: ", totaldmgslime )
    def battle_with_slime ():
        while slimes.hp>0 and players.health>0:
            main_slime()
            dead()
        print ("HURRAY! Your quickly pick up your feet and quickly hurry away")
    battle_with_slime()
    lvl_up()

    # encounter with Steve
    print("As you quickly hurried away, you saw someone in the distance")
    input()
    print("It was Steve!")
    print ()
    print ("Steve: Oh hello there ", players.name, "I've seen you left the village.")
    input()
    print("Steve: Looking for monsters?")
    input ()
    print("Steve: There's a goblin up ahead, though I do warn you; its dangerously close to the dungeon lord's lair.")
    input()
    print ("Steve: Tread carefully, I don't want to return to the villageto say another idiot went and got themselves killed.")
    input()
    print ("Steve: I'll see you around, I gotta head back to the village to sell some monster loot")
    input ()
    print()
    print()

    #encounter goblin
    print("Carefully, you continued to journey through the dungeon")
    input()
    print ("As you slowly navigated past the rocks something suddenly hit you in the back")
    input()
    print("You slowly turn around gripping your flashlight to see a goblin behind you....")
    print()

    #battle with goblin
    print("Your enemy has:", goblins.hp)
    print ("slimes deal a total damage of: ", totaldmggoblin )
    def battle_with_goblin ():
        while goblins.hp>0 and players.health>0:
            main_goblin()
        dead()
        lvl_up()
        print ("Lets hurry before it catches up!")
    battle_with_goblin()

    #encounter with orc
    print()
    input()
    print("As you scurry away, you contiue to carefully navigate the dungeon to avoid unwanted attention")
    input()
    print("This isn't a time to die when your so close to the Dungeon Lord")
    input()
    print ("You decided to take a rest and sit down to have a drink of water")
    input()
    print(...)
    input()
    print("Suddenly you heard heavy breathing before being started by a roar")
    input()
    print("You quickly get up, dropping your water")
    input()
    print("There a large orc stood ready to battle")
    print()

    #battle with orc

game()
