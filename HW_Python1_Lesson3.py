
# coding: utf-8

# In[7]:


#Easy
__author__ = "Чупраков Никита Алесандрович"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(n, nd):
    n=n*(10**nd)+0.41
    n = n//1
    return n/(10**nd)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# In[6]:


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticketnumber_list=str(ticket_number)
    if len(ticketnumber_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(ticketnumber_list[i])
        last+=int(ticketnumber_list[-i-1])
    return first==last


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


# In[22]:


#Normal

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = []
    a, b = 1, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    return res

print(fibonacci(5, 10))


# In[26]:


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    print (origin_list)
    print ('='*60)
    list = []
    while len(origin_list) > 0 :
        a = origin_list[0]
        for i in origin_list :
            if i <= a :
                a = i
        origin_list.remove(a)
        list.append(a)
    print (list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# In[31]:


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(arg, obj):
    print (obj)
    print ('='*60)
    list = []
    for i in obj : 
        if i != arg : 
            list.append(i)
    print (list)
            
list_1 = [99,99, 99,99,4, 2, 10, -12, 101, 2.5, 20, 7, 3, -11,4,4,4,0]
filter_func(4, list_1) # фильтруем 4


# In[36]:


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

A1, A2, A3, A4 = (2, 3), (0, 2), (4, 1), (6, 2)


def is_parallelogram(a, b, c, d):
#Проверка признаков параллелограмма
    p1 = False
    p2 = False
#Противополжные стороны параллельны и равны
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print("Противоположные стороны равны")
        p1 = True
    else:
        print("Противоположные стороны НЕ равны")
#Диагонали O1 и O2 в точках пересечения делятся пополам и равны
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        print("Половины диагоналей равны")
        p2 = True
    else:
        print("Половины диагоналей НЕ равны")
    print("="*60)
    if p1 and p2:
        print("Точки A1%s, A2%s, A3%s, A4%s\nОбразуют параллелограмм" %
              (a, b, c, d))
    else:
        print('Точки A1%s, A2%s, A3%s, A4%s\nНе образуют параллелограмм' %
              (a, b, c, d))

is_parallelogram(A1, A2, A3, A4)

