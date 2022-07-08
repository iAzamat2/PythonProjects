name = input('Имя: ')
surname = input ('Фамилия: ')
age = int(input('Возраст: '))
weight = int(input('Вес: '))

if age <= 30 and weight >= 50 and weight <= 120:
    print(name, surname, age, 'год', 'вес', weight, '- хорошее состояние')
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    print(name, surname, age, 'год', 'вес', weight, '- следует заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, surname, age, 'год', 'вес', weight, '- следует обратится к врачу!')