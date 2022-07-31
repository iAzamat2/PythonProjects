print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников:  '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место  '.format(i))
    members.append(name)
    i -= 1

# кто участвовал в соревновании(по алфавиту)
print('В соревновании участвовали: ', sorted(members))

# мы записали людей с конца?
members.reverse()

# нам нужно взять первые 3 места
result = members[:3]

result='Победители: {}. Поздравляем!'.format(result)
print(result)