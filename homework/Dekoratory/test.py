# def example_function(a="closure "):
#     def nest_function(b):
#         print(a * b)
#     return nest_function
#
# alias_for_exp = example_function('eee-')
# alias_for_exp(4)


# def sound_decorator(func_as_param):
#     def nested():
#         print('~hau~hau~hau~')
#         func_as_param()
#         print('~hau~hau~hau~')
#
#     return nested
#
#
#
# @sound_decorator(30)
# def quote_pet():
#     print("Pies to najlepszy przyjeciel człowieka")
#
#
# quote_pet()

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
#
#
# def print_example(name, age, smt):
#     print(name, age, smt)
#
# def print_example(*args):
#     for argument in args:
#         print(argument, end='`')
#     print()
#     print('--------------')
#
#
# print_example('ela', 13, 'hahaha')
# print_example(num=3, age=5)


# def grant_bonus(name, surname, salary_base=4200, bonus=0):
#     print(f'Employee {name} {surname} gets {salary_base} + bonus: {bonus}')

#
# def grant_bonus(*args, **kwargs):
#     print(f'args')
#     for a in args:
#         print(a)
#
#
# grant_bonus('Jan', 'Kowalski', bonus=5000, salary_base="6000")
