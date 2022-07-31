# global_var = 2
#
#
# def my_f():
#     result = global_var ** 5
#     print(result)
#
#
# def my_change_f():
#     global global_var
#     global_var = 'Строка'
#
#
# my_f()


# ================================= #

m = 'Меня видно везде'


def a():
    ma = 'Меня видно в b() и в a()'

    def b():
        print(m)
        print(ma)
        mb = 'Меня видно в с() и в b(), но не видно в a()'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Меня видно только в c()'

        c()

    b()


a()
