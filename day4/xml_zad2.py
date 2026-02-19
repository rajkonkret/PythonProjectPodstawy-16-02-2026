import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')  # wczytanie
root = tree.getroot()  # głowny tag

print("Root:", root.tag)  # Root: root

for product in root.findall("product"):
    print("Nazwa produktu:", product.get('name'))
# Root: root
# Nazwa produktu: RAJ
