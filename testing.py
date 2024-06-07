from attacks import main_blob, main_shrub, main_slime, main_goblin, main_orc, main_DL
from enemy import shrubs, slimes, orcs, goblins, dungeon_lords
from user import players


def dead():
    if players.health <= 0:
        print("you died")
        print ("LETS START OVER >:) ")
    else:
        ("ahahha")

#battle with blob
def battle_with_blob():
    main_blob()

# battling shrub code - drop is included
def battle_with_shrub ():
    while shrubs.hp > 0:
        main_shrub()
    print ("HURRAY, LETS KEEP MOVING")

# battling with slimes - drop is included
def battle_with_slime ():
    while slimes.hp>0:
        main_slime()
    print ("HURRAY, LETS KEEP MOVING")

# battling with goblins - drop is included
def battle_with_goblin ():
    while goblins.hp>0:
        main_goblin()

# battling with orcs - drop is included
def battle_with_orc ():
    while orcs.hp>0:
        main_orc()

# battling with DL - drop is included
def battle_with_DL ():
    while dungeon_lords.hp>0:
        main_DL()
        if players.health<=0:
            dead()







battle_with_DL()
print("HAHAAH")
