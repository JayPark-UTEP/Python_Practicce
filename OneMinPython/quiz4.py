#Implementing a random selecting program; Chiecken for 1, coffee for 3

#condition 1: 20 people with ID 1-20
#condition 2: Random selection but there are no duplicates
#condition 3: use shuffle and smaple

from random import *


id_list = []
i = 1;
while i <= 20:
    id_list.append(i)
    i += 1
print(id_list)

shuffle(id_list)

print("\n--------Winer--------")
print("Chicken: ", sample(id_list, 1))
print("Coffee:  ", sample(id_list, 3))
print("----Congratuation----\n")

users = range(1,21) # generating 1 to 20
users = list(users)
shuffle(users)

winners = sample(users, 4) #avoding duplicates

print("--------Winer--------")
print("Chicken: {0}".format(winners[0]))
print("Coffee:  {0}".format(winners[1:]))
print("----Congratuation----")
