# 14, 15, 1
# sqrt - корень, ** - степень, pi - число pi, fabs - модуль
# pow (x,y) возвести х в степень y, e - экспонента
import math

print("1.")
print("Введите число x: ")
x = float(input())
print("Введите число y: ")
y = float(input())
print("Введите число z: ")
z = float(input())

S = ((2*math.cos(x-(2/3)))/((1/2)+(math.sin(y))**(2)))/(1+((z**2)/(3-((z**(2))/5))))

# x = 14.26
# y = -1.22
# z = 3.5*(10**(-2))

print("При x = ", x,";", "y = ", y,";", "z = ", z,'. Ответ:', S)

print("14.")
print("Введите число x: ")
x1 = float(input())
print("Введите число y: ")
y1 = float(input())
print("Введите число z: ")
z1 = float(input())

S1 = ((y1**(x1+1))/(((math.fabs(y1-2))**(1/3))+3))+(((x1+(y1/2))/(2*(math.fabs(x1+y1))))*((x1+1)**(-1/(math.sin(z1)))))
print("При x = ", x1,";", "y = ", y1,";", "z = ", z1,'. Ответ:', S1)

print("15.")
print("Введите число x: ")
x2 = float(input())
print("Введите число y: ")
y2 = float(input())
print("Введите число z: ")
z2 = float(input())

S2 = ((((x2**(y2+1))+((math.e)**(y2-1)))/(1+(x2*(math.fabs(y2-(math.tan(z2)))))))*(1+(math.fabs(y2-x2))))+(((math.fabs(y2-x2))**2)/2)-(((math.fabs(y2-x2))**3)/3)
print("При x = ", x2,";", "y = ", y2,";", "z = ", z2,'. Ответ:', S2)


