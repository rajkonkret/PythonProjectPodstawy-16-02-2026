# xml
# język tagów

from xml.dom import minidom

root = minidom.Document()  # <?xml version="1.0" ?>
xml = root.createElement('root')  # <root>
root.appendChild(xml)

productChild = root.createElement('product')  # <product
productChild.setAttribute("name", "RAJ")  # name="RAJ"
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent="\t")
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="RAJ"/>
# </root>

with open('dane.xml', "w") as f:
    f.write(xml_str)
