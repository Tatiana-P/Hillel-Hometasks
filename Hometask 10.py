
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

import json

def read_json(data):
    with open(data, "r", encoding='utf-8') as file:
        result = json.load(file)
    return result
#######################################
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def get_surnames(data):
    surnames = []
    name = str(data.get('name'))
    for name in names:
        if len(name.split) == 1:
        surnames.append()

        elif len(name.split) == 2:
        surnames.append(name.split[1])

        elif len(name.split) == 3:
        surnames.append(name.split[2])

        else:
        pass

def sort_by_surname(data):
    sort_surname = sorted(data, key=abs(surnames))
    print(sort_surname)

#################################################################

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def sort_by_date(data):
    return data.get('years')

data_sorted = sorted(data, key=sort_by_date)
print(data_sorted)

#################################################################

# 4. Написать функцию сортировки по количеству слов в поле "text"

def sort_by_number_of_words(data):
    texts = []
for text in texts:
    text_split = text.split()
    texts.append(text_split)
sorted_texts = (sorted(texts, key=len))