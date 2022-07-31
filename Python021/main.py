numbers = [1, 5, 3, 5, 9, 7, 11]

print(sorted(numbers))

print((sorted(numbers, reverse=True)))

names = ['Max', 'Alex', 'Kate']
print(sorted(names))

cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
print(sorted(cities))


def by_count(city):
    return city[1]


print(sorted(cities, key=by_count))

print(sorted(cities, key=lambda city: city[1]))

# =================================== #

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(result)
result = list(result)
print(result)

names = ['Max', 'Leo', 'Kate']
print(list(filter(lambda x: len(x) > 3, names)))


