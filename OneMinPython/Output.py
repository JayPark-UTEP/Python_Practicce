import sys

print("Python", "Java", "JavaScript", sep = " vs ")
print("Python", "Java", "JavaScript", sep = ",", end="?")
print("What would be more fun?")
print("------------------------------------------------")
print("Python", "Java", "JavaScript", file=sys.stdout)
print("Python", "Java", "JavaScript", file=sys.stderr)
print("------------------------------------------------")

scores = {"Math":0, "Eng":50, "CS":100}
for subject, score in scores.items():
#key and value
    print(subject, score)

print("------------------------------------------------")
for subject, score in scores.items():
    print(subject.ljust(5), str(score).rjust(5), sep=":")
print("------------------------------------------------")
for num in range(1, 21):
    print("Waiting Number : " + str(num).zfill(3))
print("------------------------------------------------")
# answer = input("Enter any value: ")
# print(type(answer)) #any input stored as string
# print("Entered " + answer
# )

print("#################################################")
#Keep empty space, sort to right and get 10 points
print("{0: > 10}".format(500)) 
#+ for positive, - for negative
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#sort to left, fill blank space with _
print("{0:_<+10}".format(500)) 
print("{0:_<10}".format(500)) 
#Print , by 1000
print("{0:,}".format(1000000000))
#Print , by 1000 and +-
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
#Get 30 spaces print ^ and print , by 1000 and +-
print("{0:^<+30,}".format(1000000000))
#Decimal
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
