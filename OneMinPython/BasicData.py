my_list = ['cake1', 'cake2', 'cake3', 'cake3']
empty_list = []
print(my_list)
print(my_list[2])
print(my_list[0:2])
print(empty_list)

print('cake2' in my_list)
print(len(my_list))
my_list[3] = 'cake4'
print(my_list)
new_list = ['Drink1', 'Drink2', 'Drink3']
new_list += my_list

print(new_list)

#tuple
#Data can not be changed later
my_tuple = ('car1', 'car2', 'car3')
print(my_tuple.count('car1'))