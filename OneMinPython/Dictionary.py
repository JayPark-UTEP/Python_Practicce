cabinet = {3: "Josh", 100: "Amy"}
print(cabinet[3])
print(cabinet[100])
print("--------------------------")
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "Available"))
print(cabinet.get(3, "Available"))
print(cabinet)
print("--------------------------")

print(3 in cabinet)
print("--------------------------")

cabinet[5] = "Bryan"
print(cabinet[5])
print(cabinet)
print("--------------------------")

del cabinet[3]
print(cabinet)
print("--------------------------")

print(cabinet.keys())
print("--------------------------")
print(cabinet.values())
cabinet.clear()
print(cabinet)