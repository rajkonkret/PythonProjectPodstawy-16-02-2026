# import fun8

# # print(fun8.all_params(1, 2, 3, 4))
# fun8.all_params(1, 2, 3, 4)
# # a=1, b=2
# # c=3, d=4

import pakiet

# pakiet.powitanie() # AttributeError: module 'pakiet' has no attribute 'powitanie'

from pakiet import fun

fun.powitanie()  # Jestem pakietem

import pakiet.fun as pk  # alias
pk.powitanie() # Jestem pakietem
