import random


def generate_level_ennemy(heroe_level):
    number = (-1, 1)
    ennemy_level = heroe_level + random.choice(number)
    return ennemy_level


def fight_ennemy(heroe_level, ennemy_level, floor_tower, life, money, updating= True):
    is_winning = is_player_winning(heroe_level, ennemy_level)
    heroe_level, floor_tower, updated_life, money_update = fight_result(is_winning, heroe_level, floor_tower, life, money, updating)
    return heroe_level, floor_tower, updated_life, money_update


def fight_result(is_winning, heroe_level, floor_tower, life, money, updating= True):
    if is_winning:
        heroe_level_up, floor_update, money_update = winning_battle(heroe_level, floor_tower, money, updating)
        print('Nouvel étage atteint : ', floor_update, '\nLevel up !!', heroe_level_up,'\nIl vous reste : ', life, " points de vie.")
        return heroe_level_up, floor_update, life, money_update
    else:
        updated_life = loose_battle(life)
        print('Vous restez à l\'étage : ', floor_tower, '\nLevel : ', heroe_level,'\nIl vous reste : ', updated_life, " points de vie.")
        return heroe_level, floor_tower, updated_life, money


def is_player_winning(heroe_level, ennemy_level):
    if heroe_level >= ennemy_level:
        return True
    else:
        return False


def winning_battle(heroe_level, floor_tower, money, updating=True):
    print("Victoire !")
    heroe_level_up = update_heroe_level(heroe_level, updating)
    floor_update = update_floors_tower(floor_tower, updating)
    updated_money = update_money(money, 0.20)
    return heroe_level_up, floor_update, updated_money


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


def generate_trap(floor_tower):
    trap = random.randint(1,10)+floor_tower
    return trap


def update_money(money, amount):
    return round((money + amount),2)

heroe_level = 1
life = 5
floor_tower = 1
trap = generate_trap(floor_tower)
is_trapped = False
money = 0.00

while True:
    if is_trapped:
        trap = generate_trap(floor_tower)
        is_trapped = False
    if floor_tower %20==0 and 1<= life <5 and money >=2:
        drink = input("Veux-tu payer 2€ pour récupérer 1 point de vie? \noui/non: ")
        if drink == "oui":
            life = update_life(life, 1)
            money = update_money(money, -2)
    if floor_tower == trap:
        print("Vous déclenchez un piège et perdez un point de vie.")
        life = update_life(life, -1)
        is_trapped = True
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
                heroe_level, floor_tower, life, money = fight_ennemy(heroe_level, ennemy_level, floor_tower, life, money, False)
                is_winning = is_player_winning(heroe_level, ennemy_level)            
            if life > 0:
                new_ennemy_level = generate_level_ennemy(heroe_level)
                heroe_level, floor_tower, life, money = fight_ennemy(heroe_level, new_ennemy_level, floor_tower, life, money)    
        elif floor_tower % 20 == 0:
            life = update_life(life, -2)
            print("Aie, le héros perd 2 points de vie. Mais la victoire est assurée !")
            heroe_level, floor_tower, life, money = fight_result(True, heroe_level, floor_tower, life, money)
        elif floor_tower % 15 == 0:
            print("Victoire instantannée, on passe au niveau suivant !")
            heroe_level, floor_tower, life, money = fight_result(True, heroe_level, floor_tower, life, money)            
        else:
            heroe_level, floor_tower, life, money = fight_ennemy(heroe_level, ennemy_level, floor_tower, life, money)
            print("=============================================")
    else:
        print("Vous êtes mort à l'étage : ", floor_tower, "\nVotre héros a atteint le niveau : ", heroe_level)
        break

