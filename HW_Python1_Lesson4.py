
# coding: utf-8

# In[4]:


#Easy
__author__ = "Чупраков Никита Алесандрович"

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random 

my_list = []

for i in range(10):
    a = random.randint(-100,100)
    my_list.append(a)

print("Сгенерированный список чисел: ", my_list)
sq_list = [a ** 2 for a in my_list]
print("Список, элементы которого являются квадратами элементов исходного списка: ", sq_list)


# In[7]:


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.    

fruit_list = ['банан', 'апельсин', 'персик', 'яблоко', 'груша']
another_list = ['киви', 'банан', 'персик', 'яблоко', 'грейпфрут']
sort_list = list(set (fruit_list) & set (another_list))
print(sort_list)


# In[10]:


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = []

for i in range(10):
    a = random.randint(-100,100)
    my_list.append(a)

print("Сгенерированный список чисел: ", my_list)
sort_list = [i for i in my_list if i % 3 == 0 and i >=0 and i % 4 !=0]
print(sort_list)


# In[18]:


#Normal

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

#с помощью re
import re
line_str = re.findall(r'[a-z]+', line)
print('Символы в нижнем регистре с использованием модуля re: \n',line_str)
print('='*60)

#без re
symbol = list(map(lambda x: chr(x), list(range(65,91)))) # Преобразуем список в список букв A-Z
line_new = list(line)
 
for i, element in enumerate(line_new[:]):
    for element_2 in symbol:
        if element == element_2:
            line_new[i] = ' '

line_2 =''.join(line_new).split(' ')
 
line_str_2 = [i for i in line_2 if i != '']
print('Символы в нижнем регистре без использованием модуля re: \n',line_str_2)
print('='*60)


# In[23]:


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Решение с помощью re
line_2_str = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print('Список с использованием модуля re: \n',line_2_str)
print('='*60)
 
# Решение без re 
symbol_1 = list(map(lambda x: chr(x), list(range(65, 91)))) # Преобразуем список в список букв A-Z
symbol_2 = list(map(lambda x: chr(x), list(range(97, 123)))) # Преобразуем список в список букв a-z
line_new = list(line_2)
 
lst = []
i = len(line_new) - 1
# Находим  символ в верхнем регистре после которого стоят еще два символа в верхнем регистре
while i >= 0:
    if line_new[i] in symbol_2:
         lst.append(line_new[i])
    elif line_new[i] in symbol_1 and i <= len(line_new) - 3 and line_new[i+1] in symbol_1 and line_new[i+2] in symbol_1:
        lst.append(line_new[i])
    else:
        lst.append(' ')
    i -= 1
lst.reverse() # Переворачиваем список
 
i = 0
lst_2 = []
registr = True  # Начальное условие поиска сортировки символов в верхнем регистре

# Фильтрация списка.
while i <= len(lst)-1:
    if lst[i] in symbol_2:
        registr = True
    if lst[i] in symbol_1 and lst[i-1] in symbol_2 and lst[i-2] in symbol_2:
        lst_2.append(lst[i])
        registr = False
    elif lst[i] in symbol_1 and registr == False:
        lst_2.append(lst[i])
    else:
        lst_2.append(' ')
    i += 1
line_2 =''.join(lst_2).split(' ') # Преобразование в строку и разбиение по пробелам
 
line_str_3 = [i for i in line_2 if i != ''] # Формирование списка из строки
print('Список без использованием модуля re: \n',line_str_3)
print('='*60)


# In[40]:


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
from itertools import groupby
 
MAX_NUM = 2500
 
my_list = [random.randint(0,9) for i in range(MAX_NUM)]
my_list = ''.join(list(map(lambda x: str(x), my_list)))
print(my_list)

# Запись в файл
path = 'HW_Python1_Lesson4\\' + 'script' + '.txt'
with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(my_list))

# Чтения файла
with open(path, 'r', encoding='UTF-8') as file:
    line_1 = list(file.read())

# Выведение самой длинной последовательности одинаковых цифр
result = max((list(g) for k, g in groupby(line_1)), key=len)
print("Самоя длинная последовательность одинаковых цифр: ", result)

