def person_info(name, age, city):
    result = f'{name}, {age} года(а) проживает в городе - {city}'
    return result


print(person_info('Василий', 21, 'Москва'))


# ====================================== #

def get_max(a, b, c):
    result = max([a, b, c])
    return result


result = get_max(1, 5, 3)
print(result)

# ======================================== #

player_name = input('Введите имя игрока ')

player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy_name = input('Введите имя врага ')

enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor': 1.0
}


def get_damage(damage, armor):
    return damage / armor


def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage


attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)
