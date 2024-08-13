import random


def generate_level_ennemy(heroe_level):
    number = (-1, 1)
    ennemy_level = heroe_level + random.choice(number)
    return ennemy_level


def fight_ennemy(heroe_level, ennemy_level, floor_tower, life, updating= True):
    is_winning = is_player_winning(heroe_level, ennemy_level)
    heroe_level, floor_tower, updated_life = fight_result(is_winning, heroe_level, floor_tower, life, updating)
    return heroe_level, floor_tower, updated_life


def fight_result(is_winning, heroe_level, floor_tower, life, updating):
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
    heroe_level_up = update_heroe_level(heroe_level)
    floor_update = update_floors_tower(floor_tower, updating)
    return heroe_level_up, floor_update


def loose_battle(life):
    print('Perdu')
    return life - 1


def update_floors_tower(floor_tower, updating):
    if updating:
        return floor_tower + 1
    else:
        return floor_tower


def update_heroe_level(heroe_level):
    return heroe_level + 1


heroe_level = 1
life = 5
floor_tower = 50

while True:
    if life > 0:
        ennemy_level = generate_level_ennemy(heroe_level)
        if floor_tower % 50 == 0:
            print("Deux ennemis te font front !")
            new_ennemy_level = generate_level_ennemy(heroe_level)
            heroe_level, floor_tower, life = fight_ennemy(heroe_level, ennemy_level, floor_tower, life, False)
            if life > 0:
                heroe_level, floor_tower, life = fight_ennemy(heroe_level, new_ennemy_level, floor_tower, life)     
        else:
            heroe_level, floor_tower, life = fight_ennemy(heroe_level, ennemy_level, floor_tower, life)
            print("=============================================")
    else:
        print("Vous êtes mort à l'étage : ", floor_tower, "\nVotre héros² a atteint le niveau : ", heroe_level)
        break