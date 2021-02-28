from math import sqrt
a = int(input("Введите длину первого катета: "))
b = int(input("Введите длину второго катета: "))

c = sqrt(a**2 + b**2)

print("Длина гипотенузы: ", c)