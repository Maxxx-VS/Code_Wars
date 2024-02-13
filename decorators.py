# ###
# def outer():
#     def div (a, b):
#         return a / b
#     a1 = div
#     return a1
#
# b = outer()
# print(b(2, 5))
#
# ###
#
# def outer(func):
#     def inner(*args, **kwargs):
#         print(*args, **kwargs)
#         print('Доп функционал')
#         return func(*args, **kwargs)
#
#     return inner
#
# def rr():
#     print("rr stering")
#
# def div(a,b):
#     return a / b
#
#
# cc = outer(rr)
# print(cc())
#
# ###
#
# def my_decorator(func):
#     def wrapper():
#         print("Функционал перед запуском")
#         func()
#         print("Функционал после запуска")
#     return wrapper
# @my_decorator
# def hi():
#     print("Hello worlf")
#
# hi()

import time
def time_decor(func):
    def wrapper():
        stat_time = time.time()
        func()
        end_time = time.time()
        print(f"Функция работала - {end_time - stat_time}")
    return wrapper

@time_decor
def hi():
    a = 0
    for i in range(30000000):
        a += 1
    print(a)

hi()