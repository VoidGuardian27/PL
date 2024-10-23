# 14 Вариант
# 1 Найти максимальный элемент численного массива и поменять его местами с
# минимальным.

from random import randint
l = [randint(1, 99) for i in range(5)]
print(l)
lmax = 0
lmin = 0
for i in range (1, len(l)):
    if l[i] > l[lmax]:
        lmax = i
    if l[i] < l[lmin]:
        lmin = i
l[lmin], l[lmax] = l[lmax], l[lmin]
print(l)