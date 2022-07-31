# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    # пишем строку байт
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'w', encoding='utf-8') as f:
    # пишем строку байт
    f.write('Привет мир')

# открываем файл в рижиме чтения байтов
with open('bytes.txt', 'rb') as f:
    # читаем байты
    result = f.read()
    print(result)
    print(type(result))
    # декодируем для получения строки
    s = result.decode('utf-8')
    print(s)
