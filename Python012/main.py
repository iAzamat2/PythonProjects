# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
#
# print(type(cities))
# print(cities)
#
# cities = set(cities)
#
# print(cities)
# print(type(cities))

# ======================================== #

# cities = {'Las Vegas', 'Paris', 'Moscow'}
# print(cities)
# cities.add('Burma')
# print(cities)
# cities.add('Moscow')
# print(cities)
#
# cities.remove('Moscow')
# print(cities)
#
# print(len(cities))
#
# print('Paris' in cities)
#
# for city in cities:
#     print(city)

# ============================== #

# Max взял эти вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла эти вещи:
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги?
print(max_things | kate_things)
# какие вещи повторяются?
print(max_things & kate_things)
# какие вещи взял Max, но не взяла Kate?
print(max_things - kate_things)
# какие вещи взяла Kate, но не взял Max?
print(kate_things - max_things)
