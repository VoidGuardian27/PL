# 1
# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B
# включительно.

a = int(input("Введите число А (оно должно быть меньше или равно числу B: "))
b = int(input("Введите число B: "))

if a <= b:
    for i in range(a, b+1):
        print(i)
else:
    print("Ошибка: число А больше числа B")



