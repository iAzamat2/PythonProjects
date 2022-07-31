# import math
# import random as rd
#
# print(math.pi)
#
# print(math.sin(38))
#
# print(rd.randint(1, 10))
#

# ============================== #

# from math import *
# from random import randint, randrange
#
# print(pi)
# print(sin(30))
#
# print(randint(1, 10))


# ================================== #

# import math
#
# # 1. найти длину окуржности с определленым радиусом
#
# r = 100
# print(2 * r * math.pi)
#
# # 2. найти площадь окружности с определенным радиусом
#
# r = 100
# print((r ** 2) * math.pi)
# print((math.pow(r, 2)) * math.pi)
#
# # 3. по координатам 2-х точек определить расстояние между ними
#
# x1 = 10
# y1 = 10
# x2 = 50
# y2 = 100
# l = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print(l)
#
# # 4. найти факториал числа 9
#
# print(math.factorial(9))

# ======================================== #

from random import randint, choice, sample, shuffle

# 1. загадать случайное число от 0 до 100

print(randint(0, 100))

# 2. выбрать победеителя лотереий из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']

print(choice(players))

# 3. выбрать 3-х победеителей лотереий из списка players

print(sample(players, 3))

# 4. перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)
