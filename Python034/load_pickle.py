import pickle

# открываем файл
with open('person.dat', 'rb') as f:
    # сразу читаем объект из файла с помощью pickle
    person = pickle.load(f)

print(person)