# dekorator
# przyjmuje inną funkcję jako argument
# wykorzystuje konstrukcje funkcji wewnętrznej
from colorama import init, Fore, Style

# pip install colorama

init(autoreset=True)


def dekor(fun):
    def wew():
        print("Dodatkowe działanie")
        return fun()

    return wew


@dekor
def hej():
    print("Hej!!!")


hej()


# po dodaniu dekoratora:
# Dodatkowe działanie
# Hej!!!

def color_decorator(fun):
    def wrapper():
        result = fun()
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


@color_decorator
def napis():
    return "HELLO WORLD"


print(napis())
print("\033[35mHello\033[0m")
