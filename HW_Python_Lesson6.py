
# coding: utf-8

# In[15]:


# Easy
__author__ = "Чупраков Никита Алесандрович"

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimeter(self):
        self.perimeter = (self.AB + self.BC + self.CA)
        return (self.perimeter)

    def area(self):
        self.perimeter /=2
        self.area =  round(math.sqrt(self.perimeter*(self.perimeter - self.AB)*(self.perimeter - self.BC)* (self.perimeter - self.CA)),2)
        return (self.area)

    def height(self):
        self.area *=2
        self.height =  round((self.area / self.CA),2)
        return (self.height)

a_x = int(input("Введите координаты треугольника.\nВведите a_x: "))
a_y = int(input("Введите a_y: "))
b_x = int(input("Введите b_x: "))
b_y = int(input("Введите b_y: "))
c_x = int(input("Введите c_x: "))
c_y = int(input("Введите c_y: "))

my_triangle = Triangle(a_x, a_y, b_x, b_y, c_x, c_y)
print('Периметр: ', my_triangle.perimeter())
print('Площадь: ', my_triangle.area())
print('Высота: ', my_triangle.height())


# In[21]:


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)
        self.AD = round(math.sqrt(int(math.fabs(((d_y - a_y) ** 2) + ((d_x - a_x) ** 2)))), 2)
        self.BD = round(math.sqrt(int(math.fabs(((d_y - b_y) ** 2) + ((d_x - b_x) ** 2)))), 2)
        self.CD = round(math.sqrt(int(math.fabs(((d_y - c_y) ** 2) + ((d_x - c_x) ** 2)))), 2)
        
    def isisosceles(self):
        if self.AB == self.CD:
            return True
        else:
            return False
    
    def perimeter(self):
        self.perimeter = (self.AB + self.BC + self.CA + self.AD + self.BD + self.CD)
        return (self.perimeter)

a_x = int(input("Введите координаты трапеции.\nВведите a_x: "))
a_y = int(input("Введите a_y: "))
b_x = int(input("Введите b_x: "))
b_y = int(input("Введите b_y: "))
c_x = int(input("Введите c_x: "))
c_y = int(input("Введите c_y: "))
d_x = int(input("Введите d_x: "))
d_y = int(input("Введите d_y: "))

my_trapezoid = Trapezoid(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)

print('Длинна строны АВ = {}, ВС = {}, СА = {}, AD = {}, BD = {}, CD = {}'.format(my_trapezoid.AB, my_trapezoid.BC, my_trapezoid.CA, 
                                                       my_trapezoid.AD, my_trapezoid.BD, my_trapezoid.CD))
print('Равнобедренность: ', my_trapezoid.isisosceles())

print('Периметр: ', my_trapezoid.perimeter())

