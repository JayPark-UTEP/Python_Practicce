from asyncio.windows_events import NULL
from hashlib import new


ev1 = 10000
ev2 = 20000
ev3 = 'Fighting'

print(ev1, ev2, ev3)

q = 5/2     #2.5
a = 5//2    #2
b = 5%2     #1
c = (5**2)  #5^2 = 25

print(q, a, b, c)

print(True and True)    #True
print(True or True)     #True
print(not True)         #False

a = {1, 2, 3}
print('p' in 'print')   #True
print(1 in a)           #True
print('a' not in 'print') # True
print(5 not in a)       #True


print(bool(True))       #True
print(bool(False))      #False
a = 1
b = NULL
print(bool(a))          #True
print(bool(b))          #False
'''comments'''

lang = 'PYTHON'
print(lang[0])
print(lang[-1], lang[5])
print(lang[2:-1])

str = ''' today I went to rec
and pick up Milo'''

print(str)

str = 'Hello World this is the King of the world'

print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.swapcase())
print(str.split())

print(str.startswith('Hello'))
print(str.endswith('world'))
print(str.replace('King', 'Queen'))
print(str.find('King'))

print('개발 언어에는 {1},{0} 등이 있어요'.format('python', 'java'))
print("I am {age} years old and I like {color}".format(age = 20, color="Red"))
age = 27
color = "Blue"
print(f"I am {age} years old and I like {color}")

#next line \n
print("I am going to Virginia on June 20th. \n And comming back on July 26th")

#print "" in string
print("I am going to take \"Statistic\" and \"Numerical Analysis\" this Summer" )

#print \ in string
print("c:\\Users\\Jpark\\Desktop")

#moving pointer to the front
print("REd Apple\rPine") # Erase rist 4 chars becasue Pine

print("Redd\bApple")

#tab
print("Red\tApple")