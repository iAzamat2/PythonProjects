a = [1, 1, 1, 2, 2, 2, 3, 4]
b = [2, 4, 5]

# result = set(a) - set(b)
#
# print(list(result))

for number in a[:]:
    if number in b:
        a.remove(number)

print(a)

# =============================== #

date = '01.01.2014'

d, m, y = date.split('.')

print(d, m, y)

months = {
    '01': 'января',
    '11': 'ноября'
}

days = {
    '01': 'первое',
    '02': 'второе'
}

result = f'{days[d]} {months[m]} {y} года.'
print(result)

# =========================================== #

numbers = [1, 1, 2, 3, 3, 4, 4, 4, 5, 1, 2, 7]

result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)

print(result)