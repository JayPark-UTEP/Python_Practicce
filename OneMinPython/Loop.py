for waiting_num in [0, 1, 2, 3, 4]:
    print("Waiting numbers are : {0}".format(waiting_num))
print()
for waiting_num in range(5, 10):
    print("Waiting numbers are : {0}".format(waiting_num))

starbucks = ["Josh", "Albert", "Rubi", "Jay"]

for customer in starbucks:
    print("{0}, order is ready". format(customer))

#While
customer = "Park"
index = 5
while index >= 1:
    print("{0}, your order is ready. {1}.".format(customer, index))
    index -= 1
    if index == 0:
        print("Last call")
print("@@Thanks for visiting")
print()

person = "Unknown"

# while person != customer:
#     print("{0}, coffee is ready.".format(customer))
#     person = input("What is your name? ")

###Continue and break
absent = [2, 5]
no_book = [7] 
for student in range(1, 11):
    if student in absent:
        print("{0}, did not come to school".format(student))
        continue
    elif student in no_book:
        print("{0}, stay after school! ".format(student))
        break
    print("{0}, read the page".format(student))
    print("Next")
print()

#For loop in one sentence
student = [1, 2, 3, 4, 5]
print(student)
student = [i+100 for i in student]
print(student)

print()

student_names = ["Josh", "Albert", "Rubi", "Jay"]
student_names_length = [len(i) for i in student_names]
print(student_names)
print(student_names_length)