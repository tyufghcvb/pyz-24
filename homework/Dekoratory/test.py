# def example_function(a="closure "):
#     def nest_function(b):
#         print(a * b)
#     return nest_function
#
# alias_for_exp = example_function('eee-')
# alias_for_exp(4)


def sound_decorator(func_as_param):
    def nested():
        print('~hau~hau~hau~')
        func_as_param()
        print('~hau~hau~hau~')

    return nested



@sound_decorator(30)
def quote_pet():
    print("Pies to najlepszy przyjeciel człowieka")


quote_pet()

#
# def uppercase_decorator(func_in):
#     def nested(a):
#         txt= func_in(a)
#         return txt.upper()
#     return nested
#
#
# @uppercase_decorator
# def quot(a):
#     return a
#
#
# print(quot("jajajjaa"))

