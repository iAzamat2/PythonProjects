# is_has_name = False
# name = 'Max' if is_has_name else 'Empty'
# print(name)
#
# is_one = True
# number = 1 if is_one else 2
# print(number)
#
# is_russian = False
# print('Привет' if is_russian else 'Hello')

# =================================== #

# # слово -> СлОвО
#
# word = 'Привет'
#
# result = []
#
# for i in range(len(word)):
#     letter = word[i]
#     letter = letter.lower() if i % 2 != 0 else letter.upper()
#     result.append(letter)
#
# result = ''.join(result)
# print(result)

# ============================= #

password = input('Введите пароль: ')

print('Вы авторизованы' if password == 'secret' else 'Вход запрещен')
