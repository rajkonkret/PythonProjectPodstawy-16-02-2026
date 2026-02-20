import tkinter as tk
from tkinter import filedialog


def wybierz_plik():
    plik = filedialog.askopenfilename(title="Wybierz plik")

    if plik:
        print("Wybrano plik:", plik)


root = tk.Tk()
root.withdraw()  # ukrycie głownego okienka

wybierz_plik()
