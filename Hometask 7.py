# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random as rnd

rand_list = [rnd.randint(1, 100) for _ in range(20)]
print("rand_list", rand_list)


#############################################

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random
# в диапазоне от -10 до 10 по каждой оси.

vertex = ["A", "B", "C"]
# vertex - вершины треугольника
triangle = {key: tuple(rnd.randint(-10,10) for _ in range(2)) for key in vertex}
print("Triangle:", triangle)

#############################################

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "Hot Offer, Buy Now"

def my_print(my_str:str):
    """Prints changed string
    Args:
        my_str(str) - The string before changing.
    """
    print(f"***{my_str}***")

#############################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

persons = [{"name": "John", "age": 15},
 {"name": "Bill", "age": 50},
 {"name": "Kate", "age": 25},
 {"name": "Max", "age": 40},
 {"name": "Jack", "age": 45}]

#Вроде правильно все написала и сверила с видео, но почему-то у меня выдает ошибку: TypeError: 'int' object is not iterable
min_age = min(person["age"] for person in persons)
[print(person["name"]) for person in persons if min(person["age"])==min_age]

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

longest_name = max(len(person["name"]) for person in persons)
[print(person["name"]) for person in persons if len(person["name"])==longest_name]

my_print = lambda condition: [print(person["name"]) for person in persons if eval(condition)]
my_print(person["age"]==min_age)
my_print(len(person["name"])==longest_name)

# в) Посчитать среднее количество лет всех людей из списка.

avr = sum(person["age"] for person in persons)/len(persons)
print("avr:", avr)

#############################################

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

my_dict_1 = {"a":1, "b":11, "c":3, "d":4}
my_dict_2 = {"e":5, "f":6, "b":7, "h":8}

intersection_keys = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
print("intersection_keys:", intersection_keys)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

different_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
print("different keys: ", different_keys)


# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

different_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys())
new_dict = {key: my_dict_1[key] for key in different_keys}
print("new dictionary: ", new_dict)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

unique_keys = list(my_dict_1.keys() ^ my_dict_2.keys())
unique_my_dict_1 = {key: value for key, value in my_dict_1.items() if key in unique_keys}
unique_my_dict_2 = {key: value for key, value in my_dict_2.items() if key in unique_keys}
intersection_keys = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
common_keys = {key: [my_dict_1[key], my_dict_1[key]] for key in intersection_keys}
merged_dict = {**unique_my_dict_1, **unique_my_dict_2, **common_keys}
print("merged dict: ", merged_dict)
