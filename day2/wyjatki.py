# wyjątki - błedy podczas wykonywannia programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-16-02-2026\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1 - program wykonany z błędem
print("Dalsza część programu")

try:
    # print(5 / 0)
    # int("A")
    # print("A" * "23")
    # raise KeyError # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład Wartości")
except TypeError:
    print("Bład Typu")
except Exception as e:
    print("Bład:", e)
else:  # gdy nie ma błędu
    print("Wynik:", wynik)
finally:  # wykona sie zawsze
    print("kolejne obliczenie")

print("Dalsza część programu po obsłudze wyjątków")
# Dalsza część programu
# Bład Wartości
# Dalsza część programu po obsłudze wyjątków
# Dalsza część programu
# Bład:
# Dalsza część programu po obsłudze wyjątków

# try - except - [else - finally]
