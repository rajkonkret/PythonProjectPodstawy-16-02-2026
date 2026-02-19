import shutil
from pathlib import Path

# base_path = Path('../ops_example')  # w katalogu nadrzędnym
base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

# usunięcie katalogu jeśli istnieje
if base_path.exists() and base_path.is_dir():
    # Recursively delete a directory tree
    shutil.rmtree(base_path)

base_path.mkdir()  # tworzy katalog

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# nie ma katalogu A, nie mogę utworzyc katalogu B
# path_d.mkdir()  # FileNotFoundError: [Errno 2] No such file or directory: 'ops_example/A/D'

path_b.mkdir(parents=True)  # parents=True - tworzy wszystkie potrzebne katalogi w drzewie

# katalog C zostanie utworzony bo już istnieje nadrzędny katalog A
path_c.mkdir()

for i in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    pass