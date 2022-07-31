# friends = ['Max', 'Leo', 'Kate']
# print(friends)
# print(type(friends))
# friend = friends[0]
# print(friend)
# print(type(friend))
#
# friend = {
#     'name': 'Max',
#     'age': 23
# }
#
# print(friend)
# print(type(friend))
#
# print(friend['age'])
#
# friend['has_car'] = True
#
# print(friend)
#
# friend['has_car'] = False
#
# print(friend)
#
# del friend['age']
#
# print(friend)
#
# if 'age' in friend:
#     print('Есть возраст')
#
# if 'has_car' in friend:
#     print('Есть машина')

# ================================= #

friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
# for key in friend.keys():
#     print(key)
#     print(friend[key])
#
#
# for key in friend:
#     print(key)
#     print(friend[key])

# по значениям
# for val in friend.values():
#     print(val)

# пары ключ значение
# for item in friend.items():
#     print(item)

for key, val in friend.items():
    #print(key)
    print('ключ: {}, значение: {}'.format(key,val))

