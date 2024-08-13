import random


def generate_level_ennemy(heroe_level):
    number = (-1, 1)
    ennemy_level = heroe_level + random.choice(number)
    return ennemy_level


def fight_ennemy(heroe_level, ennemy_level, floor_tower, life, updating= True):
    is_winning = is_player_winning(heroe_level, ennemy_level)
    heroe_level, floor_tower, updated_life = fight_result(is_winning, heroe_level, floor_tower, life, updating)
    return heroe_level, floor_tower, updated_life


def fight_result(is_winning, heroe_level, floor_tower, life, updating= True):
    if is_winning:
        heroe_level_up, floor_update = winning_battle(heroe_level, floor_tower, updating)
        print('Nouvel étage atteint : ', floor_update, '\nLevel up !!', heroe_level_up,'\nIl vous reste : ', life, " points de vie.")
        return heroe_level_up, floor_update, life
    else:
        updated_life = loose_battle(life)
        print('Vous restez à l\'étage : ', floor_tower, '\nLevel : ', heroe_level,'\nIl vous reste : ', updated_life, " points de vie.")
        return heroe_level, floor_tower, updated_life


def is_player_winning(heroe_level, ennemy_level):
    if heroe_level >= ennemy_level:
        return True
    else:
        return False


def winning_battle(heroe_level, floor_tower, updating=True):
    print("Victoire !")
    heroe_level_up = update_heroe_level(heroe_level, updating)
    floor_update = update_floors_tower(floor_tower, updating)
    return heroe_level_up, floor_update


def loose_battle(life):
    print('Perdu')
    return update_life(life, -1)


def update_life(life, health_point):
    return life + health_point


def update_floors_tower(floor_tower, updating):
    if updating:
        return floor_tower + 1
    else:
        return floor_tower


def update_heroe_level(heroe_level, updating):
    if updating:
        return heroe_level + 1
    else:
        return heroe_level


heroe_level = 1
life = 5
floor_tower = 100

while True:
    if life > 0:
        ennemy_level = generate_level_ennemy(heroe_level)
        
        if floor_tower % 10 == 0 and life < 5:
            print("Vous récupérez 1 point de vie.")
            life = update_life(life, 1)
        if floor_tower % 50 == 0:
            print("Deux ennemis te font front !")
            is_winning = False
            while not is_winning and life > 0:
                ennemy_level = generate_level_ennemy(heroe_level)
                heroe_level, floor_tower, life = fight_ennemy(heroe_level, ennemy_level, floor_tower, life, False)
                is_winning = is_player_winning(heroe_level, ennemy_level)            
            if life > 0:
                new_ennemy_level = generate_level_ennemy(heroe_level)
                heroe_level, floor_tower, life = fight_ennemy(heroe_level, new_ennemy_level, floor_tower, life)    
        elif floor_tower % 20 == 0:
            life = update_life(life, -2)
            print("Aie, le héros perd 2 points de vie. Mais la victoire est assurée !")
            heroe_level, floor_tower, life = fight_result(True, heroe_level, floor_tower, life)
        elif floor_tower % 15 == 0:
            print("Victoire instantannée, on passe au niveau suivant !")
            heroe_level, floor_tower, life = fight_result(True, heroe_level, floor_tower, life)            
        else:
            heroe_level, floor_tower, life = fight_ennemy(heroe_level, ennemy_level, floor_tower, life)
            print("=============================================")
    else:
        print("Vous êtes mort à l'étage : ", floor_tower, "\nVotre héros a atteint le niveau : ", heroe_level)
        break

