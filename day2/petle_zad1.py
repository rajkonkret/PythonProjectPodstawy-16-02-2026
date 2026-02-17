# pętla - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for _ in range(15):  # niema zmienna
    print("Test podłoga - niema zmienna")
    print(_)  # można odczytać wartość
# Test podłoga - niema zmienna
# 13
# Test podłoga - niema zmienna
# 14

for i in range(5):
    print(i + 2)
    print(i * 2)
