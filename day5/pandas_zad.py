import pandas as pd
import matplotlib.pyplot as plt

# pip install matplotlib

df = pd.read_csv("dane_p.csv")
df.plot(x="miesiac", y="sprzedaz")

plt.show()
