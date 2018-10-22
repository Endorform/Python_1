
# coding: utf-8

# In[ ]:


# Easy
__author__ = "Чупраков Никита Алесандрович"


# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа, 
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86 
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
# случайная карточка. 
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
	
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71   
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87      
#       16 49    55 77    88    
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать 
# модуль random: http://docs.python.org/3/library/random.html


# In[5]:


import random, copy

MAX_BARREL = 90
DIGITS_IN_CARD = 15
DIGITS_IN_LINE = 5


def gen_card():
    # Комбинация 15 рандомных цифр без повторений
    num_comb = random.sample(range(1, MAX_BARREL + 1), DIGITS_IN_CARD)
    # Делим на 3 списка
    card = [sorted(num_comb[i:i + DIGITS_IN_LINE]) for i in range(0, len(num_comb), DIGITS_IN_LINE)]
    return card


def gen_barr_list():
    return random.sample(range(1, MAX_BARREL + 1), 90)


def get_barrel(barr_list):
    return barr_list.pop()


def show_card(card):
    card = copy.deepcopy(card)  
    placeholders = ' '.join(['{:>2}' for i in range(9)])  
    for line in card:
        for space in ' ' * 4:
            line.insert(random.randint(0, len(line) - 1), space)  # Рандомно помещаем 4 пустых места
    return [placeholders.format(*line) for line in card]


def update_card(card, barrel):
    # Меняем число на -
    for line in card:
        yield ['-' if x == barrel else x for x in line]


def is_empty(card):
    for line in card:
        for elt in line:
            if elt != '-':
                return False
    return True


def barr_in_card(card, barrel):
    #Возвращает True, если число есть в карточке
    return barrel in [barrel for line in card for barrel in line]


def play_round():
    print('''Добро пожаловать в игру Лото!. Вы играете против компьютера.
Если ошибетесь - проиграете.
Генерирую карточку и перемешиваю бочонки...\n''')
    player_card, comp_card = gen_card(), gen_card()
    barrels = gen_barr_list()
    while True:  
        next_barrel = get_barrel(barrels)
        print('Следующий бочонок: {}. Осталось: {}'.format(next_barrel, len(barrels)))
        print("{0} Карточка игрока {0}\n{1}\n{2}\n{3}".format('-' * 6, *show_card(player_card)))
        print("{0} Карточка компьютера {0}\n{1}\n{2}\n{3}".format('-' * 5, *show_card(comp_card)))
        answ = 'a'
        while answ not in 'ynq':
            answ = input("Есть ли бочонок в карточке игрока? y/n или q, чтобы выйти: ")
        if answ == 'q':
            print('Хорошего дня!')
            break
        elif (answ == 'y' and barr_in_card(player_card, next_barrel)) or (answ == 'n' and not barr_in_card(player_card,
                                                                                                           next_barrel)):
            print('Правильно! \n\nСледующий ход...')
        else:
            print('Вы проиграли!')
            break
        player_card = list(update_card(player_card, next_barrel))
        comp_card = list(update_card(comp_card, next_barrel))
        if is_empty(player_card):
            print('Вы заполнили всю карточку!')
            break
        if is_empty(comp_card):
            print('Компьютер заполнил всю карточку!')
            break


play_round()

