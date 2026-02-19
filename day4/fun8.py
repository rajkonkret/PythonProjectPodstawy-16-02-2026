def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)
# a=1, b=2
# c=42, d=256

all_params(1, 2, c=89)
all_params(1, 2, 89)
# a=1, b=2
# c=89, d=256

all_params(1, 2, 89, 45)
all_params(1, 2, c=89, d=45)
all_params(1, 2, d=45)

all_params(1, 2, c=89, d=45)


# / - oddziela argumenty pozycyjne od nazwanych
# a, b - musza byc przekazane po pozycji !!!
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# all_params(a=1, b=2, c=3, d=4)

def all_params2(name, b, /, c=42, *args, d=67, **kwargs):
    print(f'{name=}')
    print(f"{b=}, {c=}, {d=}")
    print(f"{args}")
    print(f"{kwargs}")


all_params2("Radek", 1)
all_params2("Radek", 1, 2)
all_params2("Radek", 1, 2, 4, 5, 6, 7, 8, 9, 0)
all_params2("Radek", 1, 2, 4, 5, 6, 7, 8, 9, 0, d=23)  # d musi być po nazwie

all_params2("Radek", 1, 2, 4, 5, 6, 7, 8, 9, 0, d=23, g=90)
# name='Radek'
# b=1, c=2, d=23
# (4, 5, 6, 7, 8, 9, 0)
# {'g': 90}

all_params2("Radek", 1, 2, 4, 5, 6, 7, 8, 9, 0, d=23, g=90, name=90)
# name='Radek'
# b=1, c=2, d=23
# (4, 5, 6, 7, 8, 9, 0)
# {'g': 90, 'name': 90}
