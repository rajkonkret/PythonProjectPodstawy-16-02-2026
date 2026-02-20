"""
Plik okno2.py
Prosty program z użyciem Tkinter — okno z labelką i przyciskiem zamykającym.
Uruchomienie:
    python okno2.py               # otworzy okno i będzie działać interaktywnie
    python okno2.py "Cześć" --demo  # otworzy okno z etykietą i automatycznie zamknie po 1s (przydatne do testów)
"""

import sys
import tkinter as tk
from typing import Optional


def create_window(text: str = "Witaj, to jest labelka!") -> tk.Tk:
    """Tworzy i zwraca główne okno z labelką i przyciskiem zamknięcia."""
    root = tk.Tk()
    root.title("Okno2 - Labelka")

    label = tk.Label(root, text=text, font=("Segoe UI", 14))
    label.pack(padx=20, pady=12)

    btn = tk.Button(root, text="Zamknij", command=root.destroy)
    btn.pack(pady=(0, 12))

    return root


if __name__ == "__main__":
    # Tekst labelki można podać jako pierwszy argument CLI (opcjonalny).
    text_arg: Optional[str] = None
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        text_arg = sys.argv[1]

    text = text_arg or "Witaj, to jest labelka!"
    root = create_window(text)

    # Flaga --demo zamyka okno automatycznie po 1s — przydatne do automatycznych testów.
    if "--demo" in sys.argv:
        root.after(1000, root.destroy)

    root.mainloop()