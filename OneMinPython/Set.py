#No duplication
#not ordered

my_set = {1,1,2,3,3,4}

print(my_set)

java = {"Josh", "Rubi", "Jay", "Albert"}
python = set(["John", "Jay"])

#intersection
print(java & python)
print(java.intersection(python))

#Union
print(java | python)
print(java.union(python))

#Subtraction Y java N python
print(java - python)
print(java.difference(python))

python.add("Rubi")
java.remove("Albert")

