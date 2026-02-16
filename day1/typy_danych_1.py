wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float

print(wiek + rok)  # 2073
print(wiek - rok)  # -1979
print(wiek * rok)  # 95222
print(wiek / rok)  # 0.02319842053307009 -> float

print(12 / 3)  # 4.0

print(2026 / 47)  # 43.1063829787234
print(2026 // 47)  # 43 - część całkowita dzielenia

print(rok % wiek)  # 5, modulo, reszta z dzielenia
print(43 * 47)  # 2021
print(2026 - 2021)  # 5

print(10 % 3)  # reszta 1

print(wiek ** rok)  # potęgowanie

print(len(str(wiek ** rok)))  # długość 3388

# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

# Process finished with exit code 0 - kod działa poprawnie

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0


