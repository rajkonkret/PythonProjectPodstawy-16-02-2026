# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print('Komunikat')

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(50 * "-")
print(licznik)

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
