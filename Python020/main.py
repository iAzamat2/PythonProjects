# def some_f():
#     return 10
#
#
# result = some_f()
# print(result)
#
# a = some_f
# print(a)
#
# print(type(a))
#
# print(a())


# ================================ #

# def f():
#     print('hello from other f')
#
#
# def to(f_param):
#     f_param()
#
#
# to(f)

# ====================================== #

def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# def is_even(number):
#     return number % 2 == 0


# def is_not_even(number):
#     return number % 2 != 0


# def big4(number):
#     return number > 4


# print(my_filter(numbers, is_even))
# print(my_filter(numbers, is_not_even))
# print(my_filter(numbers, big4))

# =============================== #
# lambda функции

print(my_filter(numbers, lambda number: number % 2 == 0))

print(my_filter(numbers, lambda number: number % 2 != 0))

print(my_filter(numbers, lambda number: number > 4))
