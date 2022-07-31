# import os
#
# # Имя операционной системы
# print(os.name)
#
# # текущая рабочая директория
# print(os.getcwd())
#
# # создаем новый путь
# new_path = os.path.join(os.getcwd(), 'new_f')
#
# # создаем папку по новому пути
# os.mkdir(new_path)

# ============================================ #

# import sys
#
# # путь до интерпретатора
# print(sys.executable)
# # информация о платформе
# print(sys.platform)
# # выход из python
# sys.exit()
#
# print('Этот код уже не выполним')

#  ========================================== #

# import sys
#
# print(sys.path)
# print(type(sys.path))
#
# for p in sys.path:
#     print(p)

# sys.path.append('D:')
# import mymodule

# ========================================= #

import sys, os

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)

# ================================================ #
