# 4
# Дано несколько чисел. Вычислите их сумму. Сначала вводите количество
# чисел N, затем вводится ровно N целых чисел. Постройте решение так, чтобы
# использовалось минимальное количество переменных.

s = 0
print("Введите количество чисел: ")
n = int(input())
if n <= 0:
    print("Количество чисел не должно быть меньше или равно 0")
    exit()
print("Введите числа: ")
for a in range(0, n):
    a = int(input())
    s += a
print(s)
