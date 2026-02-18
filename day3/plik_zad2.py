import chardet

# pip install chardet

# with open("test.log", "r") as file:
#     lines = file.read()
# print(lines)

# odczyt binarny - rb
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'PArametr 1\r\nPArametr 2\r\nPArametr 3\r\nPArametr 4\r\nDodane\r\nDodane\r\nDodane jescze jedno\r\nDod\xc5\x9bane jescze jedno\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.668135593220339, 'language': ''}

# po dodaniu więcej polskich liter w tekscie mamy prawidłowy wynik
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie:", encoding)  # Kodowanie: utf-8
print("Dokładność:", confidence)  # Dokładność: 0.938125

print(50 * "_")
print(raw_data.decode(encoding=encoding))
# __________________________________________________
# PArametr 1
# PArametr 2
# PArametr 3
# PArametr 4
# Dodane
# Dodane
# Dodane jescze jedno
# Dodśąźńane jescze jedno
