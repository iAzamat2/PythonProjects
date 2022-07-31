# читаем объект из файла

# открываем файл
with open('person.dat', 'rb') as f:
    # теперь нам надо знать как мы записывали объект
    # прочитаем файл в список
    result = f.readlines()

# теперь воссоздаем исходный объект
person = {}
# первый элемент это имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телефоны
phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# получили исходный объект. Это было достаточно тяжело. А что если он немного изменится?
print(person)
