
# coding: utf-8

# In[16]:


#Easy
__author__ = "Чупраков Никита Алесандрович"

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Already exists")
try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")


# In[7]:


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

list = os.listdir()
for i in list:
    print(i)


# In[8]:


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_cwd():
    shutil.copy(r'HW_Python1_Lesson5.py', r'HW_Python1_Lesson5_dupl.py')

