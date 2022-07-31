# print(abs(-7))
#
# numbers = [5, 15, 7, 1, -9, 0]
# print(max(numbers))
# print(min(numbers))
#
# print(round(10.9872, 2))
#
# print(sum(numbers))
#
# winners = ['Leo', 'Max', 'Kate']
# for number, winner in enumerate(winners, 1):
#     print(number, winner)
#


numbers = []

for i in range (3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

