import pandas

# pip install pandas

# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-16-02-2026\day1> pip list
# Package           Version
# ----------------- -----------
# chardet           5.2.0
# librt             0.8.0
# mypy              1.19.1
# mypy_extensions   1.1.0
# numpy             2.4.2
# pandas            3.0.1
# pathspec          1.0.4
# pip               25.1.1
# python-dateutil   2.9.0.post0
# six               1.17.0
# typing_extensions 4.15.0
# tzdata            2025.3

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   100.00
# 2    3  tomorrow   900.00
# 3    4     today  1200.00
# 4    5     today  7200.00
# 5    6     today   199.99

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='str')

print(data.values)
# [[1 'today' 200.0]
#  [2 'today' 100.0]
#  [3 'tomorrow' 900.0]
#  [4 'today' 1200.0]
#  [5 'today' 7200.0]
#  [6 'today' 199.99]]

print(data.items)
# <bound method DataFrame.items of    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   100.00
# 2    3  tomorrow   900.00
# 3    4     today  1200.00
# 4    5     today  7200.00
# 5    6     today   199.99>
