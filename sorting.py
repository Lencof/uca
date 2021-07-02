"""
В файле используется класс Sort, содержащий:
1) создание случайного списка
2) 3 варианта сортировки списка
"""

import os
import sys
import random

# create class Sort:
class Sort:

    def __init__(self, count):
        self.count = count
        print('\r')

    def generate_random_list(self, count):
        """ Создание случайного списка натуральных неповторяющихся чисел, принадлежащих [1; count] """
        randlist = []
        while len(randlist) < count:
            r = random.randrange(1, count + 1)
            if r not in randlist:
                randlist.append(r)
        return randlist

    def pusirki(self):
        """ Пузырьковая сортировка """
        print('-' * self.count, self.pusirki.__doc__, '-' * self.count,)
        rnd_list = self.generate_random_list(self.count)
        print(rnd_list)  # исходный список

        # Алгоритм
        cyc = 1
        while cyc == 1:
            cyc = 0
            for i in range(1, len(rnd_list)):
                if rnd_list[-i] < rnd_list[-i-1]:
                    rnd_list[-i], rnd_list[-i-1] = rnd_list[-i-1], rnd_list[-i]
                    cyc = 1
                    print(rnd_list)

    def vibor(self):
        """ Сортировка выбором """
        print('-' * self.count, self.pusirki.__doc__, '-' * self.count,)
        rnd_list = self.generate_random_list(self.count)
        print(rnd_list)  # исходный список

        # Алгоритм
        i = 0
        while i < len(rnd_list) - 1:
            min_num = min(rnd_list[i:])
            for ind in range(0, len(rnd_list)):
                if rnd_list[ind] == min_num:
                    rnd_list[ind], rnd_list[i] = rnd_list[i], rnd_list[ind]
                    break
                ind += 1
            i += 1
            print(rnd_list)

    def vstavki(self):
        """ Сортировка вставками """
        print('-' * self.count, self.pusirki.__doc__, '-' * self.count,)
        rnd_list = self.generate_random_list(self.count)
        print(rnd_list)  # исходный список

        # Алгоритм
        ind = 1
        while ind < len(rnd_list):
            for i in range(0, len(rnd_list[:ind])):
                if rnd_list[ind-i] < rnd_list[ind-i-1]:
                    rnd_list[ind-i], rnd_list[ind-i-1] = rnd_list[ind-i-1], rnd_list[ind-i]
                    print(rnd_list)
                else:
                    break
            ind += 1






