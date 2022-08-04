import math

if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет т.к. первое условие ложь')

# первая истина
print(0 or [] or 8 or 5)

# последняя ложь
print(0 or [] or () or {})
