min_dict = {}
max_dict = {}
my_dict = {'1':23, '2':45, '3':67, '4':23}
#temp = min(my_dict.values())
#print(temp)
res = {k:v for k,v in my_dict.items() if v == min(my_dict.values())}
min_dict.update(res)
print(min_dict)
