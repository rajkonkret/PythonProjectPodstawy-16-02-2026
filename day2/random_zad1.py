import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int, od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # 0 do 4

print(random.random())  # float, 0.623313019054461, od 0 do 0.9999999
print(random.random() * 7)  # float, 3.759230444026488, od 0 do 6.9999999

print(round(random.random() * 9))  # 1

lista = [67, 45, 32, 68, 90, 42, 49]
print(lista[random.randrange(len(lista))])  # 42 element

print(random.choice(lista))  # 67, - element

# stworzyc listę kul
# wylosowac kulę z listy
# wyświetlić kule
# usunąc kule z listy
lista_kul = list(range(1, 50))  # od 1 do 49
kula = random.choice(lista_kul)
lista_kul.remove(kula)
print(kula)  # 6

print(random.choices(lista_kul, k=6))  # [31, 41, 32, 31, 46, 17], z powtórzeniami

print(random.sample(lista_kul, k=6))  # [4, 46, 33, 20, 31, 44]
# k: nie przepisujemy!
print(random.sample(lista_kul, 6))  # [40, 18, 15, 6, 39, 11]
