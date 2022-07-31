# def hello_max():
#     print('Hello', 'Max')
#
#
# hello_max()
#
#
# def hello(who):
#     print('Hello', who)
#
#
# hello('Leo')

# =============================== #

# def greeting(say, *args):
#     print(say, args)
#
#
# greeting('Leo', 'Hi')
#
# # не верно
# greeting('Hi', 'Leo')
# #greeting(say='Hi', who='Leo')

# ================================== #

def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age=20, has_car=True)
