# import fun8

# # print(fun8.all_params(1, 2, 3, 4))
# fun8.all_params(1, 2, 3, 4)
# # a=1, b=2
# # c=3, d=4

import pakiet

print(50 * "-")
# pakiet.powitanie() # AttributeError: module 'pakiet' has no attribute 'powitanie'
# po dodaniu w __info__.py metoda info() działa
pakiet.info() # Wersja: v1.79.01.234

from pakiet import fun

fun.powitanie()  # Jestem pakietem

import pakiet.fun as pk  # alias

pk.powitanie()  # Jestem pakietem
