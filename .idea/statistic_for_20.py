import random
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Организация общего списка значений для анализа
excel_data = pd.read_excel('statistic_for.xlsx', usecols='A:C')
data = pd.DataFrame(excel_data,columns=['Числа'])
data_1 = data['Числа'].to_list()

print('Импорртированный список из файла xlsx : ',data_1)
data_3 = []
for i in data_1:
    j = i.split(',')
    data_3.append(j)
print(data_3)

#Разбиение общего списка на списки первого и второго сетов
data_ftup = []
data_stup = []
for i in data_3:
    for j in range(len(i)):
        if j <=3:
            data_ftup.append(int(i[j]))
        else:
            data_stup.append(int(i[j]))
            

print('Первый сет :',len(data_ftup),data_ftup)
print('Второй сет :',len(data_stup),data_stup)


sat_dict = {}
sat_dict_1 = {}
for j in range(1,21):
    c = data_ftup.count(j)
    sat_dict.update({str(j):c})
    c_1 = data_stup.count(j)
    sat_dict_1.update({str(j):c_1})

print('Статистика первого сета : ',sat_dict)
print('Статистика второго сета : ',sat_dict_1)


# Максимум и минимум первого и второго сета
set_dict_max = {}
set_dict_min = {}


def min_max_set(set_dict):
    res = {k: v for k, v in set_dict.items() if v == min(set_dict.values())}
    set_dict_min.update(res)
    res_1 = {k: v for k, v in set_dict.items() if v == max(set_dict.values())}
    set_dict_max.update(res_1)


min_max_set(sat_dict)
print('Максимум первого сета :',set_dict_max)
print('Минимум первого сета :',set_dict_min)

set_dict_max.clear()
set_dict_min.clear()

min_max_set(sat_dict_1)
print('Максимум второго сета :',set_dict_max)
print('Минимум второго сета :',set_dict_min)

#Сортировка словарей первого и второго сетов
sorted_fset_max = dict(sorted(sat_dict.items(), key=lambda x:x[1], reverse=True))
print('Сортировка первого сета по максимуму: ',sorted_fset_max)
sorted_fset_min = dict(sorted(sat_dict.items(), key=lambda x:x[1]))
print('Сортировка первого сета по минимуму: ',sorted_fset_min)
sorted_secset_max = dict(sorted(sat_dict_1.items(), key=lambda x:x[1], reverse=True))
print('Сортировка второго сета по максимуму: ',sorted_secset_max)
sorted_secset_min = dict(sorted(sat_dict_1.items(), key=lambda x:x[1]))
print('Сортировка второго сета по минимуму: ',sorted_secset_min)


# Построение графиков первого и второго сетов
plt.grid(True)
plt.plot(list(sat_dict.keys()), list(sat_dict.values()))
plt.yticks(np.arange(min(list(sat_dict_1.values())), max(list(sat_dict_1.values())) +1))
plt.plot(list(sat_dict_1.keys()), list(sat_dict_1.values()))
plt.show()

#Выборка средних значений сетов
def midll_set(dict_set):
    midll_set = {}
    for k, v in dict_set.items():
        if max(dict_set.values()) - v  > 2 and v - min(dict_set.values())  > 2:
         midll_set.update({k:v})
    return midll_set
midll_set_1 = midll_set(sat_dict)
midll_set_2 = midll_set(sat_dict_1)
print('Усредненный первый сет:',midll_set_1)
print('Усредненный второй сет:',midll_set_2)

def rand_nam(dict_set):
    rand_set = []
    for i in range(1, 5):
            i = list(dict_set.items())
            k, v = i[randint(0, len(dict_set)-1)]
            dict_set.pop(k)
            rand_set.append(k)
    return rand_set


print(rand_nam(midll_set_1))
print(rand_nam(midll_set_2))


