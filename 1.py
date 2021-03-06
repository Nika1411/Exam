# !/usr/bin/env python3
# -*- config: utf-8 -*-

import sys

# Составить UML-диаграмму деятельности и программу для решения задачи: Дано натуральное число n (n <
# 1000). Напечатать это число русскими словами (тринадцать, сто пять, двести сорок один и т. д.).

if __name__ == '__main__':
    n = int(input('Введите натуральное число до 1000'))
    if n > 999:
        print('Вы ввели сликом большое число', file=sys.stderr)
        exit(1)

    a = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    b = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    c = {100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
         500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот',
         800: 'восемьсот', 900: 'девятьсот'}
    d = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}

    if n < 10:
        for i in a:
            if i == n:
                n1 = a.get(n)
                print(n1)

    elif 10 < n < 20:
        for i in d:
            if i == n:
                n1 = d.get(n)
                print(n1)

    if 19 <= n <= 99:
        n1 = n % 10
        n2 = n - n1
        for i in b:
            if i == n2:
                n10 = b.get(n2)
                for j in a:
                    if j == n1:
                        n11 = a.get(n1)
                        print(f'{n10} {n11}')

    if n > 99:
        n1 = n % 10
        n2 = n % 100 - n1
        n3 = n - n % 100
        if n2 == 10:
            for k in c:
                if k == n3:
                    n100 = c.get(n3)
                    n2 = n % 100
                    for i in d:
                        if i == n2:
                            n22 = d.get(n2)
                            print(f'{n100} {n22}')
        elif n2 == 0:
            for k in c:
                if k == n3:
                    n100 = c.get(n3)
                    for j in a:
                        if j == n1:
                            n11 = a.get(n1)
                            print(f'{n100} {n11}')
        else:
            for k in c:
                if k == n3:
                    n100 = c.get(n3)
                    for i in b:
                        if i == n2:
                            n10 = b.get(n2)
                            for j in a:
                                if j == n1:
                                    n11 = a.get(n1)
                                    print(f'{n100} {n10} {n11}')
