# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).

import os

with open("/Users/tatiana/PycharmProjects/Hillel-Hometasks/domains.txt", "r") as file:
    domains = []
    for line in file.readlines():
        domains.append(line.strip("."))
print(domains)

######################################################################

# 2. Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)

with open("/Users/tatiana/PycharmProjects/Hillel-Hometasks/names.txt", "r") as file:
    surnames = ['\n'.join([line.split()[1] for line in file.readlines()])],
print(surnames)

######################################################################

# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com

from random import randint
import string

def create_random_email():
 """Creates email in format: surname.number@string of 5-7 characters.domain"""
    part_1 = random.choice(surnames)
    part_2 = randint(100, 999)
    part_3 = ''.join(random.choices(string.ascii_lowercase, k = randint(5,7)))
    part_4 = random.choice(domains)

print(part_1,".", part_2,"@", part_3,".", part_4)