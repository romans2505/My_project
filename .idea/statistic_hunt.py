

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

excel_data = pd.read_excel('statistic_hunt.xlsx', usecols='A:C')
data = pd.DataFrame(excel_data,columns=['Числа'])
data_1 = data['Числа'].to_list()
print('Импорртированный список из файла xlsx : ',data_1)
data_3 = []
for i in data_1:
    j = i.split(',')
    data_3.append(j)
#print(data_3)
data_ftup = []
data_stup = []
for i in data_3:
    for j in range(len(i)):
        if j <=3:
            data_ftup.append(int(i[j]))
        else:
            data_stup.append(int(i[j]))
print('Первый сет :',data_ftup)
print('Второй сет :',data_stup)
sat_dict = {}
sat_dict_1 = {}
for j in range(1,21):
    c = data_ftup.count(j)
    sat_dict.update({str(j):c})
    c_1 = data_stup.count(j)
    sat_dict_1.update({str(j):c_1})

print('Статистика первого сета : ',sat_dict)
print('Статистика второго сета : ',sat_dict_1)
set_dict_max1 = {}
set_dict_min1 = {}
i, j = max((i, j) for j, i in sat_dict.items())
if int(j) <= max(sat_dict.values()):
    set_dict_max1.update({j:i})
print('Максимум первого сета :',set_dict_max1)
i, j = min((i, j) for j, i in sat_dict.items())
if  int(j) <= min(sat_dict.values()):
    set_dict_min1.update({j:i})
print('Минимум первого сета :',set_dict_min1)
set_dict_max2 = {}
set_dict_min2 = {}
i, j = max((i, j) for j, i in sat_dict_1.items())
if int(j) <= max(sat_dict_1.values()):
    set_dict_max2.update({j:i})
print('Максимум второго сета :',set_dict_max2)
i, j = min((i, j) for j, i in sat_dict_1.items())
if  int(j) <= min(sat_dict_1.values()):
    set_dict_min2.update({j:i})
print('Минимум второго сета :',set_dict_min2)
sorted_fset_max = dict(sorted(sat_dict.items(), key=lambda x:x[1], reverse=True))
print('Сортировка первого сета по максимуму: ',sorted_fset_max)
sorted_fset_min = dict(sorted(sat_dict.items(), key=lambda x:x[1]))
print('Сортировка первого сета по минимуму: ',sorted_fset_min)
sorted_secset_max = dict(sorted(sat_dict_1.items(), key=lambda x:x[1], reverse=True))
print('Сортировка второго сета по максимуму: ',sorted_secset_max)
sorted_secset_min = dict(sorted(sat_dict_1.items(), key=lambda x:x[1]))
print('Сортировка первого сета по минимуму: ',sorted_secset_min)
plt.plot(list(sat_dict.keys()), list(sat_dict.values()))
plt.plot(list(sat_dict_1.keys()), list(sat_dict_1.values()))
plt.grid(True, which='both', linestyle='--', linewidth=10,axis= 'both')
plt.show()






