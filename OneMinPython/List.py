my_list = ['cake1', 'cake2', 'cake3', 'cake3']
empty_list = []
print(my_list)
print(my_list[1])
print(my_list[-1])
print(my_list[0])
print(empty_list)
if('cake2' in my_list):
    print("Cake2 is in the list the length of the list is ", len(my_list))
    print("{0} is in the list the length of the list is {1}".format("Cake2", len(my_list)))
if(my_list[3] == 'cake3'):
    print("Therea are {0} of cake 3".format(my_list.count("cake3")))
    my_list.remove("cake3")
    my_list.append("cake4")
print(my_list)
print("-------------------------------------")

new_list = ['Drink1', 'Drink2', 'Drink3']
my_list += new_list
print(my_list)
print("-------------------------------------")

pet_list = []
pet_list.append("Cat")
pet_list.append("Rabit")
pet_list.append("Lion")
print(pet_list)
cat = pet_list.index("Cat")
pet_list.insert(cat+1, "Dog")
print(pet_list)
print(pet_list.pop())
print(pet_list)
pet_list.remove("Cat")
print(pet_list)
pet_list.clear()
print(pet_list)
print("-------------------------------------")
pet_list.extend(new_list)
print("1", pet_list)

#sort()
#reverse()
#clear()
print("-------------------------------------")

