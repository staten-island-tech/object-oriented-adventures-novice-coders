from attacks import attacking_shrub, again_shrubs, equations_shrub, main
from enemyATK import shrub_attacking
from enemy import shrubs


def cheking ():
    main()
    while shrubs.hp > 0:
        print ("this is shrubs hp" , shrubs.hp)
        print("running")
        shrub_attacking()
        main()
    
    print ("cheking victory")

cheking()