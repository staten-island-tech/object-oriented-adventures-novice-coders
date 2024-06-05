from attacks import attacking_shrub, again_shrubs, equations_shrub
from enemyATK import shrub_attacking
from enemy import shrubs


equations_shrub()
def cheking ():
    if shrubs.hp!= 0:
        shrub_attacking()
        equations_shrub()
        cheking()
if shrubs.hp!= 0:
    cheking()