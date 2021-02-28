from math import pi
h = int(input("Введите высоту цилиндра: "))
d = int(input("Введите диаметр цилиндра: "))
r = d/2
s = 2*pi*r*(h+r)
print("Площадь поверхности цилиндра: ", s)