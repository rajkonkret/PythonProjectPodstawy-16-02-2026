# decimal - biblioteka do działania na liczbach zmmiennoprzecinkowych
# pozwala lepiej zarządzać zaokrgleniami

from decimal import Decimal

kwota1 = Decimal("10.25")
kwota2 = Decimal("5.50")

print(kwota1 + kwota2)  # 15.75

precyzja = Decimal("0.00")

roznica = kwota1 - kwota2
print("Różnica:", roznica)  # Różnica: 4.75
print("Różnica (zaokrąglone):", roznica.quantize(precyzja))  # Różnica (zaokrąglone): 4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podakiem:", kwota_z_podatkiem)
print("Kwota z podatkiem (zaokrąglone):", kwota_z_podatkiem.quantize(precyzja))
# Kwota z podakiem: 12.6075
# Kwota z podatkiem (zaokrąglone): 12.61

print(Decimal("0.3"))  # 0.3
print(Decimal(0.3))
# 0.299999999999999988897769753748434595763683319091796875
