# 2
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в
# порядке возрастания, если A < B, или в порядке убывания в противном случае.

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

if a < b:
    for i in range(a, b+1):
        print(i)
elif a >= b:
    for i in range(a, b-1, -1):
        print(i)