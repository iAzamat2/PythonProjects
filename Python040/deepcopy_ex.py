import copy

a = [1, 2, [1, 2]]

b = copy.deepcopy(a)
b[2][1] = 200

# список a не изменился
print(a)
