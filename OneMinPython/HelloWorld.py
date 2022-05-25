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