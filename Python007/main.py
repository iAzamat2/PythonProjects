# пустой список
empty_list = []

# можно объявить список и сразу заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - list
print(type(friends))

# Как и в строке для списка доступны индексы (с 0)
print('Второй друг: ', friends[1])
print('Первый друг с конца', friends[-1])

# Так же можно применить срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])

# ======================================================= #

friends = ['Max', 'Leo', 'Kate']

print(friends)

print(len(friends))

friends.append('Ron')

print(friends)

print(len(friends))

print(friends.pop())

print(friends)

friends.clear()

print(friends)

friends = ['Max', 'Leo', 'Kate']

friends.remove('Kate')

print(friends)

del friends[0]

print(friends)

# ================================ #
hero = 'Superman'
#hero = 'Super'

if hero.find('man') != -1:
    print('Есть')

if 'man' in hero:
    print('Есть')

goals = {'стать гуру языка python', 'здоровье', 'накормить кота'}

if 'здоровье' in goals:
    print('Все хорошо')

# ==================================== #

