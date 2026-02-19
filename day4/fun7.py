def connet(**opcje):  # dowolna ilośc argumentów nazwanych (keyword)
    print(opcje)


connet()  # {}
connet(a=10)  # {'a': 10}
connet(a=10, b=90, c=78, name="Radek", age=90)


# {'a': 10, 'b': 90, 'c': 78, 'name': 'Radek', 'age': 90}

def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4)  # (1, 2, 3, 4) {}
all_args(1, 2, 3, 4, a=10, b=34)  # (1, 2, 3, 4) {'a': 10, 'b': 34}
all_args(a=10, b=90)  # () {'a': 10, 'b': 90}


def radek_random(*args, k=0):
    print(args, k)


radek_random(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
radek_random(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, k=10)  # k musi byc po nazwie po jest po *args
