# # строка байт
# sb = b'Ad'
#
# # по ascii таблице должно получиться 65
#
# print(sb[0])
#
# # по ascii таблице должно получиться 100
# print(sb[1])

s = 'Hello world Мир'

sb = s.encode('utf-8')

print(sb)
print(type(sb))

s = sb.decode('utf-8')
print(s)
print(type(s))
