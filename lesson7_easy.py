# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

# AB = input("Длина первого катета: ")
# AC = input("Длина второго катета: ")
#
# AB = float(AB)
# AC = float(AC)
#
# BC = math.sqrt(AB ** 2 + AC ** 2)
#
# S = (AB * AC) / 2
# P = AB + AC + BC
# print("Площадь треугольника: %.2f" % S)
# print("Периметр треугольника: %.2f" % P)
#
#
# a = float(input('Введите сторону А: '))
# b = float(input('Введите сторону B: '))
# c = float(input('Введите сторону C: '))
# if (a+b)>=c:
#     p = (a + b + c) / 2
#     hA = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a
#     hB = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / b
#     hC = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / c
#     print('Высота с точки А',round(hA,3))
#     print('Высота с точки B', round(hB,3))
#     print('Высота с точки C', round(hC,3))
# else:
#     print('Треугольника не существует')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class trapezoid():
    def __init__(self, name, x1, y1, x2, y2, x3, y3, x4, y4):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def __str__(self):
        return self.name

    def proverka(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))

        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

    def side(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)

    def perimeter(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        return (a + b + c + d)

    def area(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        return ((a + b) / 2) * (math.sqrt((c ** 2) - ((((b - a) ** 2) + (c ** 2) - (d ** 2)) / (2 * (b - a)))))


fis_trap = trapezoid('one', 0, 0, 2, 2, 4, 2, 6, 0)
fis_trap.proverka()
fis_trap.side()
print(fis_trap.perimeter())
print(fis_trap.area())
fis_trap1 = trapezoid('two', 0, 0, 3, 3, 6, 3, 9, 0)
fis_trap1.proverka()
fis_trap1.side()
print(fis_trap1.perimeter())
print(fis_trap1.area())
if fis_trap.perimeter() > fis_trap1.perimeter():
    print('Perimetr' + str(fis_trap))
else:
    print('Perimetr' + str(fis_trap1))