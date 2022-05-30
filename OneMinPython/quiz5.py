''' You are a taxi driver
There are 50 customers are matched
How many customers you can pick them up?

condition1: Driving time is random mins 5;50 mins
condition2: You can only select customers who have 5-15 mins driving time
'''

from random import *

customer_count = 0 #customers can pick up

for i in range(1, 51): # generating 1-50
    time = randrange(5, 51) # random driving time
    if 15 >= time >= 5:
        print("[0] {0}th customer (Driving time: {1}mins)".format(i, time))
        customer_count +=1
    else: 
        print("[ ] {0}th customer (Driving time: {1}mins)".format(i, time))

print("Total customer: {0}".format(customer_count))