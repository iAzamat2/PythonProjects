friend = 'Максим'

first_letter = friend[0]
print('Первая буква имени друга', first_letter)

print(friend[1])

print(friend[4])

print(friend[-1])

print(friend[-2])

print(friend[1:4])

print(friend[:4])

print(friend[3:])

print(type(friend[1:4]))

# ============================================= #

friends = 'Максим Леонид'
print(friends)

print(len(friends))

print(friends.find('Лео'))

print(friends.split())

friends = 'Максим;Леонид'

print(friends.split(';'))

print(friends.isdigit())

number = '123'
print(number.isdigit())

print(friends.upper())

print(friends.lower())

# =================================== #

# # форматирование строк
name = 'Leo'
age = 30
# 1. Конкатенация
hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)

# 2. %
hello_str = 'Привет %s тебе %d лет' % (name, age)
print(hello_str)

# 3. format
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)

# ===================== #

top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов'
start = top5.find('1')
end = top5.find('4')

top3 = top5[start: end]

result = 'Поздравляем {} с успехом'.format(top3.upper())

print(result)
