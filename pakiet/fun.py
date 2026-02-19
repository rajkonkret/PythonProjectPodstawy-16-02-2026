def powitanie():
    print("Jestem pakietem")


def info():
    print("Wersja: v1.79.01.234")

print(__name__)
# pakiet.fun - gdy jako import
# __main__ - gdy uruchamiasz fun.py
if __name__ == '__main__':

    powitanie()