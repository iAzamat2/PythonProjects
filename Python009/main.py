friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

# Типы данных
print(type(friend_name))
print(type(friends))
print(type(roles))

# Индексация
print(friend_name[1])
print(friends[1])
print(roles[1])

# Срезы
print(friend_name[1:])
print(friends[1:])
print(roles[1:])

# Длина
print(len(friend_name))
print(len(friends))
print(len(roles))

if 'Max' in friends:
    print('У меня есть этот друг')

if 'M' in friend_name:
    print('Буква М есть в имени друга')

# for

for friend in friends:
    print(friend)

for letter in friend_name:
    print(letter)

# while
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

for role in roles:
    print(role)
    
print('end')