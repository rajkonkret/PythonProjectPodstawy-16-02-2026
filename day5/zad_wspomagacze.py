# chatgpt, gemini, grok, copilot
# claude code https://claude.ai/login
# agenci kodawania: copilot, claude, gemini, tabnine, codeium,
# codegeex, codepal, codeassist, codewhisperer, codegpt, codex
# Pattern CTPFT
# Cel:
# Kontekst:
# Ograniczenia:
# Plan działania:
# Format odpowiedzi:
# Test poprawności:

print("dane")
print("da")
print("")
# napisz funkcje obliczajaća srednia
print("srednia")
print("srednia")
print("srednia")


def srednia(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(srednia(1, 2, 3))  # 2.0
print(srednia(10, 20, 30, 40))  # 25.0
print(srednia())  # 0


# zrob funkcje sortowanie bąbelkowe
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]


# [11, 12, 22, 25, 34, 64, 90]

# połącz listy w pary
def zip_lists(list1, list2):
    return list(zip(list1, list2))


print(zip_lists([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# kolejne zadanie
print("kolejne zadanie")
