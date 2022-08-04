import random


def game_reverse():
    min_number = 1
    max_number = 100
    result = None
    while result != '1':
        number = random.randint(min_number, max_number)
        print(number)
        result = input(
            'Загаданное число: \nРавно предложенному-> 1\nБольше предложенного -> 2\nМеньше предложенного -> 3\n')
        if result == '2':
            min_number = number + 1
        elif result == '3':
            max_number = number - 1
    print('Победа')


if __name__ == '__main__':
    game_reverse()
