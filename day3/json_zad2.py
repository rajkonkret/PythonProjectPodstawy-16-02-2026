# {
#         "description": "\u201eName mangling\u201d to mechanizm zmiany nazwy atrybut\u00f3w klasy, kt\u00f3re s\u0105 zdefiniowane jako prywatne, co ma na celu unikni\u0119cie konflikt\u00f3w nazw w klasach pochodnych.",
#         "example": "print(\"Przyk\u0142ad do: Co to jest \u201ename mangling\u201d w Pythonie?\")",
#         "id": 30,
#         "level": "podstawowy",
#         "term": "Co to jest \u201ename mangling\u201d w Pythonie?"
#     }
import json

# r - raw tekst - znaki specjalne traktuje jako zwykły tekst
resp = r'''{
         "description": "\u201eName mangling\u201d to mechanizm zmiany nazwy atrybut\u00f3w klasy, kt\u00f3re s\u0105 zdefiniowane jako prywatne, co ma na celu unikni\u0119cie konflikt\u00f3w nazw w klasach pochodnych.",
         "example": "print(\"Przyk\u0142ad do: Co to jest \u201ename mangling\u201d w Pythonie?\")",
         "id": 30,
         "level": "podstawowy",
         "term": "Co to jest \u201ename mangling\u201d w Pythonie?"
     }'''

dane = json.loads(resp)
print(dane)
print(type(dane))  # <class 'dict'>

# wypisac wszystkie klucze ze słownika
