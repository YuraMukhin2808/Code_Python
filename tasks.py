from __future__ import print_function
from numba import jit
jit(nopython=True)
from colorama import init
from colorama import Style, Back, Fore
init()
print(Fore.GREEN)
yers_list = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

print(yers_list)
print(yers_list[0])
print(yers_list[5])

things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
things.remove("salmonella")

print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]

print(surprise[-1].capitalize())

e2f = {'Dog': 'chien', 'cat': 'chat', 'warlus': 'mrose'}
f2e = {}
for english, french in e2f.items():
	f2e[french] = english

print(set(e2f.keys()))

life = {
	'animals':{
		'cats':[
			'Henri', 'Grumpy', 'Lucy'
			],
		'octopi':{},
		'emus':{}
		},
		'plants':{},
		'other':{}
		}
print(set(life['animals']['cats']))

for value in [3, 2, 1, 0]:
	print(value)
even = [number for number in range(10) if number % 2 == 0]
print(even)

guess_me = 7
start = 1
while True:
	if start < guess_me:
		print('too low')
	elif start == guess_me:
		print('too high')
	elif start > guess_me:
		print('oops')
		break
	start += 1

for value in [3, 2, 1, 0]:
	print(value)

even = [number for number in range(10) if number % 2 == 0]
squares = {key: key*key for key in range(10)}
odd = {number for number in range(10) if number % 2 ==1}

print(even)
print(squares)
print(odd)

for thing in ('Got %s' % number for number in range(10)):
	print(thing)

def good():
	return ['Harry', 'Ron', 'Hermione']

print(good())

def get_odds():
	for number in range(1, 10, 2):
		yield number
for count, number in enumerate(get_odds(), 1):
	if count == 3:
		print("The third odd number is", number)
		break

def test(func):
	def new_func(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return new_func
@test
def greeting():
	print("Greetings, Earthling")

print(greeting())

class OopsExcept(Exception):
	pass
try:
	raise OopsExcept
except OopsExcept:
	print('Caught a oops')

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns  into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)

import hou
hou.hours()

from hou import hours as info
info()

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])

class Thing():
	pass
example = Thing()

print(Thing)
print(example)

class Gres:
	lete = 'abcd'

print(Gres.lete)

class LOLSAS:
	def __init__(self):
		self.lete = 'xyz'
something = LOLSAS()

print(something.lete)

class Elment:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
hydrogen = Elment('Hydrogen', 'H', 1)
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Elment(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen = Elment(**el_dict)
print(hydrogen.name)
print(hydrogen.name)

class Elment:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
	def dump(self):
		print('name=%s, symbol=%s, number=%s' %
			(self.name, self.symbol, self.number))

hydrogen = Elment(**el_dict)
print(hydrogen.dump())

print(hydrogen)

hydrogen = Elment(**el_dict)
print(hydrogen)

class Bear:
	def eats(self):
		return 'berries'

class Rabbit:
	def eats(self):
		return 'clover'

class Octothorpe:
	def eats(self):
		return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()

print(b.eats(), r.eats(), o.eats())

class Laser:
	def does(self):
		return 'disintegrate'

class Claw:
	def does(self):
		return 'crush'

class SmartPhone:
	def does(self):
		return 'ring'

class Robot:
	def __init__(self):
		self.laser = Laser()
		self.claw = Claw()
		self.smartphone = SmartPhone()
	def does(self):
		return '''I have many attachments:\nMy laser, to %s,\nMy claw, to %s,\nMy smartphone, to %s''' % (self.laser.does(), self.claw.does(), self.smartphone.does())

robot = Robot()
print(robot.does())

import unicodedata

mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
pop_string = pop_bytes.decode('utf-8')

print(mystery)
print(unicodedata.name(mystery))
print(pop_bytes)
print(pop_string)
print(pop_string == mystery)

poem = '''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s,
And now thinks he's a %s.'''

letter = '''
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amonut} for shipping and handling. We will send
you another {product} that. in our tests, is {precent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely.
{spokesman}
{job_title}
'''
response = {
	'salutation': 'Colonel',
	'name': 'Hackenbush',
	'product': 'duck blind',
	'verbed': 'imploded',
	'room': 'conservatory',
	'animals': 'emus',
	'amonut': '$1.38',
	'precent': '1',
	'spokesman': 'Edgar Schmeltz',
	'job_title': 'Licensed Podiatrist'
}
print(letter.format(**response))

args = ('roast beef', 'ham', 'head', 'clam')
print(poem % args)

import re

mammoth = '''
We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees
Or as the leaves upon the trees
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth beware of these
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.'''

pat1 = r'\bc\w*'
pat2 = '\bc\w*'
pat3 = r'\bc\w{3}\b'
pat4 = r'\bc\w{3}'
pat5 = r'\b\w*r\b'
pat6 = r'\b\w*l\b'
pat7 = r"\b[\w\']*l\b"
pat8 = r'\b[\w\']*l\b'
pat9 = r'\b\w*[aeiou]{3}[^aeiou]\w*\b'
pat10 = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b'
print(re.findall(pat1, mammoth))
print(re.findall(pat2, mammoth))
print(re.findall(pat3, mammoth))
print(re.findall(pat4, mammoth))
print(re.findall(pat5, mammoth))
print(re.findall(pat6, mammoth))
print(re.findall(pat7, mammoth))
print(re.findall(pat8, mammoth))
print(re.findall(pat9, mammoth))
print(re.findall(pat10, mammoth))

import binascii
hex_str = '474946383910100010080000000ffffff21f9' + \
	'04010000000002c000010001000020144003b'
gif = binascii.unhexlify(hex_str)

print(len(gif))
print(gif[:6] == b'GIF89a')
print(gif[:6] == 'GIF89a')
print(type(gif))
print(type('GIF89a'))
print(type(b'GIF89a'))

import struct
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)

test1 = 'This is a test of emergency text system'
len(test1)

outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close()
with open('test.txt', 'wt') as outfile:
	outfile.write(test1)
with open('test.txt', 'rt') as infile:
	test2 = infile.read()
len(test2)
print(test1 == test2)

import csv
text = '''author.book
J R R Tolkein. The Hobbit
Lynne Truss, "Eats, Shoots & Leaves"
'''
with open('test23.csv', 'wt') as outfile:
	outfile.write(text)
with open('test23.csv', 'rt') as infile:
	books = csv.DictReader(infile)
	for book in books:
		print(book)


input("[Нажмите ENTER что-бы продолжить: ]")

def multiply(a, b):
  print(2 * 4)

print(multiply(4, 5))

def gg(a, b, c):
	return a * b * c

print(gg(4, 4, 4))

def add_func(operator):
	def inner(func):
		def thingy(*args, **kwargs):
			return operator(func(*args, **kwargs))
		return thingy
	return inner

print(add_func)

import re

def domain_name(url):
	return re.findall(r"(?:\w+\.|\/\/)(?:www\.)?(\w+)\.\w+", url)[0]

print(re)
print(domain_name)

import string

def is_pangram(va:str):
	return set(val.lower()) >= set(string.ascii_lowercase)

print(string)
print(is_pangram)

def multiply(a, b):
	a,b = list(map(digits, [a,b]))
	res = [0 for _ in range(len(a+b)-1)]
	for i,n in enumerate(b):
		for j,m in enumerate(b):
			res[i+j] += n*m
	return res

def digits(n):
	return list(map(int, str(n)))

print(3, 4)
print(digits(2))

def encode_rail_fence_cipher(string, n):
	return encode_rail_fence_cipher

print(encode_rail_fence_cipher("H !o,Wdloor", 3), "Hello, World")

def long_function_name(
		var_one, var_two, var_three,
		var_four):
	print(var_one)

my_list = [
	1, 2, 3,
	4, 5, 6,
	]

print(my_list)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elem in a:
	if elem < 5:
		print(elem)

print(list(filter(lambda elem: elem < 5, a)))
print([elem for elem in a if elem < 5])

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = [set(a) & set(b)]

import operator
g = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = dict(sorted(g.items(), key=operator.itemgetter(1)))
print(result)

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

result = {}
for d in (dict_a, dict_b, dict_c):
	result.update(d)

result = {**dict_a, **dict_b, **dict_c}

my_dict = {'a':500, 'b':5874, 'o':560, 'd':400, 'e':5874, 'f':20}

result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)

print(int('ABC', 28))

def pascal_triangle(n):
	row = [1]
	y = [0]
	for x in range(max(n, 0)):
		print(row)
		row = [left + right for left, right in zip(row + y, y + row)]

pascal_triangle(6)

def convert(seconds):
	days = seconds // (24 * 3600)
	seconds %= 24 * 3600
	hours = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)

def solve(n):
	n1 = n
	n2 = int(str(n) * 2)
	n3 = int(str(n) * 3)
	print(n1 + n2 + n3)

solve(10)

lst = [1, 2, 3, 4, 5]
print(f'Первый: {lst[0]}; последний: {lst[-1]}')

numbers = [
	386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
	399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
]

for x in numbers:
	if x == 237:
		break
	elif x % 2 == 0:
		print(x)

set_1 = set(['While', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])

print(set_1 - set_2)

def sum_digits(num):
	digits = [int(d) for d in str(num)]
	return sum(digits)

print(sum_digits(5245))

string = 'Python Software Foudation'
print(string.count('o'))

x = 5
y = 10
x, y = y, x

x = 5
y = 10
temp = x
x = y
y = temp

nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))

def all_unique(numbers):
	return len(numbers) == len(set(numbers))

from random import random

n = random() * 900 + 100
n = int(n)
print(n)

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a+b+c)

import numpy as np
a = np.array([2, 4, 6, 8, 10])
b = np.array([3, 6, 9, 12, 15])
c = np.array([4, 8, 12, 16, 20])

print(a + b * c)

def sum_for_loop(a):
	s = 0
	for x in a:
		s += x
	return s

def sum_while_loop(a):
	s = 0
	n = len(a)
	while n:
		n -= 1
		s += a[n]
	return s

def sum_recursive(a):
	if len(a) == 0:
		return 0
	return a[0] + sum_recursive(a[1:])

if __name__ == '__main__':
	t = [5, 3, 4, 1, 7]
	for f in (sum_for_loop, sum_recursive):
		print(f(t))

def combine_lists(a, b):
	len_a = len(a)
	len_b = len(b)
	if len_a < len_b:
		limit = len_a
	else:
		limit = len_b
	i = 0
	r = []
	while i < limit:
		r.append(a[i])
		r.append(b[i])
		i += 1
	return r

if __name__ == '__main__':
	a = ['a', 'b', 'c']
	b = ['A', 'B', 'C', 'D']
	print(repr(combine_lists(a, b)))

def fibonacci(n=10, a=0, b=1):
	yield a
	yield b
	b -= 2
	while n > 0:
		c = a + b
		a = b
		b = c
		yield c
		n -= 1

if __name__ == '__main__':
	for n in fibonacci(100):
		print(n)

s = "ERROR" * 9
h = '404' * 9
print(s, h)
print(len(s), len(h))

import math, random

def BinarySeach(a, x, l, r):
	def NewMiddle():
		return math.ceil((l + r)/2)

		m = NewMiddle()
		while l <= r:
			if a[m] == x:
				print('Элемент {0} был найден в позиции {1}.'.format(x, m))
				return x
			elif x > a[m]:
				l = m + 1
				m = NewMiddle()
			else:
				r = m - 1
				m = NewMiddle()
		print('Не обнаружено элемента со значением {0}.'.format(x))
N = 10
L = list()

for i in range(0, N):
	L.append(random.randint(0, 10))

L.sort()
print(L)

print(BinarySeach(L, 4, 0, N - 1))

L = max([[1, 2, 3], [4, 5, 6]], key = max)
print(L)
print('Индекс максимального элемента {0} равен {1}.'.format(max(L), L.index(max(L))))

spisok = [1,2,3,4,5,6]
spisok2 = [7,8,9,10,11]

def sommename(*args):
	print(args)

print(sommename(spisok,spisok2))

dct = {'one':1,'two':2}

for x in dct:
	print(x, '=>', dct[x])

def chentost(number):
	if number % 2 == 0:
		print('Chetnoe')
	else:
		print('Nechetnoe')

print(chentost(5))

code = 100

def add(num):
	global code
	code = num

add(50)

print(code)

x=int(input("Введите число час: "))
y=x/60
a=x%60
print(int(y))
print(int(a))

a = 5
b = 2.0
c = 1+2j
print(a, "is of type", type(a))
print(b, "is of type", type(b))
print(c, "is complex number?", isinstance(1+2j, complex))

a = 1234567890123456789
b = 0.1234567890123456789
c = 1+4j
print(a, b, c)

import pdb

x = [[1,2,3,4]] * 3
y = [[1,2,3,4] for _ in range(3)]

print(x)
print(y)

import numpy
numpy.array([])
numpy.empty(shape=(0,0))

import numpy as np

a = np.arange(9).reshape(3,3)

print(a[[2, 1, 0], :])

x = int(input("Введите число: "))
if 1 <= x <= 3: #Число от 1 до 3
	s = input("Введи строку: ")
	n = int(input("Введите кол-во повторов: "))
	i = 0
	while i < n:
		print(s)
		i += 1
elif 4 <= x <= 6: #Число от 4 до 6
	m = int(input("Введите степень: "))
	print(x ** m)
elif 7 <= x <= 9: #Число от 7 до 9
	i = 0
	while i < 10:
		x += 1
		print(x)
		i += 1
else:
	print("Ошибка ввода!")

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)

list2 = ["Mike", "", "Emma", "Kellt", "", "Brad"]
resList = list(filter(None, list2))
print(resList)

aList = [1, 2, 3, 4, 5, 6, 7]
aList = [x * x for x in aList]
print(aList)

List3 = [5, 20, 15, 20, 25, 50, 20]

def removeValue(sampleList, val):
	return [value for value in sampleList if value != val]
resList = removeValue(List3, 20)
print(resList)

bList = [100, 200, 300, 400, 500]
bList = bList[::-1]
print(bList)

import logging

def log(func):
	def wrap_log(*args, **kwargs):
		name = func.__name__
		logger = logging.getLogger(name)
		logger.setLevel(logging.INFO)

		fh = logging.FilHandler("%s.log" % name)
		fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		formatter = logging.Formatter(fmt)
		fh.setFormatter(formatter)
		logger.addHandler(fh)

		logger.info("Вызов функции: %s" % name)
		result = func(*args, **kwargs)
		logger.info("Результат: %s" % result)
		return func

	return wrap_log

def double_function(a):
	return a*2
if __name__ == "__main__":
	value = double_function(2)

def squares(start, stop):
	for i in range(start, stop):
		yield i * i
generator = squares(a, b)

def f(a):
	a = 99
	b = 88
f(b)
print(b)

def append(list=[]):
	list.append(len(list))
	return list

print(['a', 'b'])
print(append())

def append(list=None):
	if list is None:
		list = []
	list.append(len(list))
	return list

print(append([5]))

i = 'I'
j = 'J'
tmp = i
i = j
j = tmp
i,j = j,i
print(i, j)

flist = []
for i in range(3):
	flist.append(lambda: i)

print([f() for f in flist])

class User:
	def __init__(self):
		self.name = 'Ivan Ivanov'
		self.age = 16

user_obj = User()
print(user_obj.name)

def testgen(index):
	weekdays = ['sun','mon','tue','wed','thu','fri','sat']
	yield weekdays[index]
	yield weekdays[index+1]

day = testgen(0)
print(next(day), next(day))

class Vin:
	def __init__(self):
		self.name = 'Не Выключать'
		self.age = 11

vin_obj = Vin()
print(vin_obj.name)
print(vin_obj.age)

import re
result1 = re.match(r'AV', 'AV Analytics Vidhya AV')
result2 = re.match(r'Analytics', 'AV Analytics Vidhya AV')
result3 = re.search(r'Analytics', 'AV Analytics Vidhya AV')
result4 = re.findall(r'AV', 'AV Analytics Vidhya AV')
result5 = re.findall(r'AV', 'AV Analytics Vidhya AV')

print(result1)
print(result1.group(0))
print(result1.start())
print(result1.end())
print(result2)
print(result3.group(0))
print(result4)
print(result5)


finc1 = [2,4,6,8,10]
finc2 = [2,4,6,8,10]

def xlm(*age):
	print(age)

print(xlm(finc1 + finc2))

import numpy as np
a = np.array([2, 4, 6, 8, 10])
b = np.array([2, 4, 6, 8, 10])

print(a + b)

flag = input("What to calculate? (m, d, v): ")
if flag == 'm':
	d = float(input("Density: "))
	v = float(input("Volume: "))
	result = d * v
elif flag == 'd':
	m = float(input("Mass: "))
	v = float(input("Volume: "))
	result = m / v
elif flag == 'v':
	m = float(input("Mass: "))
	d = float(input("Density: "))
	result = m / d
print("%.2f" % result)

from random import random

matrix = []

for i in range(5):
	row = []
	for j in range(5):
		row.append(int(random()*10))
	matrix.append(row)

for row in matrix:
	print(row)

maxRow = 0
idRow = 0
i = 0
for row in matrix:
	if sum(row) > maxRow:
		maxRow = sum(row)
		idRow = i
	i += 1

print(idRow, '-', maxRow)

maxCol = 0
idCol = 0
for i in range(5):
	colSum = 0
	for j in range(5):
		colSum += matrix[j][i]
	if colSum > maxCol:
		maxCol = colSum
		idCol = i

print(idCol, '-', maxCol)

a = int(input("Введите первой число: "))
b = int(input("Введите второй число: "))

while a != 0 and b != 0:
	if a > b:
		a %= b
	else:
		b %= a

gcd = a + b
print(gcd)

from random import random
N = 20
array = []
for i in range(N):
	array.append(int(random()*100))
array.sort()
print(array)

number = int(input("Введите Двоичный поиск число: "))

low = 0
high = N-1
while low <= high:
	mid = (low + high) // 2
	if number < array[mid]:
		high = mid - 1
	elif number > array[mid]:
		low = mid + 1
	else:
		print("ID =", mid)
		break
else:
	print("No Такое number")

from random import random

num = round(random() * 1000, 3)
print(num)

strNum = str(num)

maxDigit = -1

for i in range(len(strNum)):
	if strNum[i] == '.':
		continue
	elif maxDigit < int(strNum[i]):
		maxDigit = int(strNum[i])

print(maxDigit)

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

print("Введите значение[png, jpg, jpeg, gif, svg]:")

file = input().split('.')
if len(file) >=2:
	fileExtension = file[-1].lower()
	if fileExtension in extensions:
		print("Yes")
	else:
		print("No")
else:
	print("The file doesn't have an extention")

str = "Yura, Ivan, Misha, Vadimer, Anton, Lech, Igor, Dima, Max"
print(str)

listWords = str.split()

idLongestWord = 0

for i in range(1,len(listWords)):
	if len(listWords[idLongestWord]) < len(listWords[i]):
		idLongestWord = i

print(listWords[idLongestWord])

a = 2
b = 3

print(a + b)

def bubble_sort(nums):
	# Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				# Меняем элементы
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				# Устанавливаем swapped в True для следующей итерации
				swapped = True

# Проверяем, что оно работает
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

def selection_sort(nums):
	# Значение i соответствует кол-ву отсортированных значений
	for i in range(len(nums)):
		# Исходно считаем наименьшим первый элемент
		lowest_value_index = i
		# Этот цикл перебирает несортированные элементы
		for j in range(i + 1, len(nums)):
			if nums[j] < nums[lowest_value_index]:
				lowest_value_index = j
		# Самый маленький элемент меняем с первым в списке
		nums[j], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# Проверяем, что оно работает
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

def insertion_sort(nums):
	# Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
	for i in range(1, len(nums)):
		item_to_insert = nums[i]
		# Сохраняем ссылку на индекс предыдущего элемента
		j = i - 1
		# Элементы отсортированного сегмента перемещаем вперёд, если они больше
		# элемента для вставки
		while j >= 0 and nums[j] > item_to_insert:
			nums[j + 1] = nums[j]
			j -= 1
		# Вставляем элемент
		nums[j + 1] = item_to_insert

# Проверяем, что оно работает
random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)

def heapify(nums, heap_size, root_index):
	# Индекс наибольшего элемента считаем корневым индексом
	largest = root_index
	left_child = (2 * root_index) + 1
	right_child = (2 * root_index) + 2

	# Если левый потомок корня — допустимый индекс, а элемент больше,
	# чем текущий наибольший, обновляем наибольший элемент
	if left_child < heap_size and nums[left_child] > nums[largest]:
		largest = left_child
	# То же самое для правого потомка корня
	if right_child < heap_size and nums[right_child] > nums[largest]:
		largest = right_child
	# Если наибольший элемент больше не корневой, они меняются местами
	if largest != root_index:
		nums[root_index], nums[largest] = nums[largest], nums[root_index]
		# Heapify the new root element to ensure it's the largest
		heapify(nums, heap_size, largest)

def heap_sort(nums):
	n = len(nums)
	 # Создаём Max Heap из списка
	# Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
	# перед первым элементом списка
	# 3-й аргумент означает повторный проход по списку в обратном направлении,
	# уменьшая счётчик i на 1
	for i in range(n, -1, -1):
		heapify(nums, n, i)

	# Перемещаем корень Max Heap в конец списка
	for i in range(n - 1, 0, -1):
		nums[i], nums[0] = nums[0], nums[i]
		heapify(nums, i, 0)

# Проверяем, что оно работает
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)

def merge(left_list, right_list):
	sorted_list = []
	left_list_index = right_list_index = 0

	# Длина списков часто используется, поэтому создадим переменные для удобства
	left_list_length, right_list_length = len(left_list), len(right_list)

	for _ in range(left_list_length + right_list_length):
		if left_list_index < left_list_length and right_list_index < right_list_length:
			# Сравниваем первые элементы в начале каждого списка
			# Если первый элемент левого подсписка меньше, добавляем его
			# в отсортированный массив
			if left_list[left_list_index] <= right_list[right_list_index]:
				sorted_list.append(left_list[left_list_index])
				left_list_index += 1
			# Если первый элемент правого подсписка меньше, добавляем его
			# в отсортированный массив
			else:
				sorted_list.append(right_list[right_list_index])
				right_list_index += 1
		# Если достигнут конец левого списка, элементы правого списка
		# добавляем в конец результирующего списка
		elif left_list_index == left_list_length:
			sorted_list.append(right_list[right_list_index])
			right_list_index += 1
		# Если достигнут конец правого списка, элементы левого списка
		# добавляем в отсортированный массив
		elif right_list_index == right_list_length:
			sorted_list.append(left_list[left_list_index])
			left_list_index += 1

	return sorted_list

def merge_sort(nums):
	# Возвращаем список, если он состоит из одного элемента
	if len(nums) <= 1:
		return nums

	# Для того чтобы найти середину списка, используем деление без остатка
	# Индексы должны быть integer
	mid = len(nums) // 2

	# Сортируем и объединяем подсписки
	left_list = merge_sort(nums[:mid])
	right_list = merge_sort(nums[mid:])

	# Объединяем отсортированные списки в результирующий
	return merge(left_list, right_list)

# Проверяем, что оно работает
random_list_of_nums = [120, 45, 68, 250, 176]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)

def partition(nums, low, high):
	# Выбираем средний элемент в качестве опорного
	# Также возможен выбор первого, последнего
	# или произвольного элементов в качестве опорного
	pivot = nums[(low + high) // 2]
	i = low - 1
	j = high + 1
	while True:
		i += 1
		while nums[i] < pivot:
			i += 1

		j -= 1
		while nums[j] > pivot:
			j -= 1

		if i >= j:
			return j

		# Если элемент с индексом i (слева от опорного) больше, чем
		# элемент с индексом j (справа от опорного), меняем их местами
		nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
	# Создадим вспомогательную функцию, которая вызывается рекурсивно
	def _quick_sort(items, low, high):
		if low < high:
			# This is the index after the pivot, where our lists are split
			split_index = partition(items, low, high)
			_quick_sort(items, low, split_index)
			_quick_sort(items, split_index + 1, high)

	_quick_sort(nums, 0, len(nums) - 1)

# Проверяем, что оно работает
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

class Auto:
	def ride(self):
		print("Riding on a ground")

class Boat:
	def swim(self):
		print("Sailing in the ocean")

class Amphibian(Auto, Boat):
	pass

a = Amphibian()
a.ride()
a.swim()
isinstance(a, Auto)
isinstance(a, Boat)
isinstance(a, Amphibian)

#Бинарный Поиск
def binary_search(list, item):
	low = 0
	high = len(list)-1#В переменных low и high хранятся границы той части списка, в которой выполняется поиск
	while low <= high:
		mid = (low + high)#Пока эта часть не сократится до одного эмелента проверяем средний элемент
		guess = list[mid]
		if guess == item:#Значение найдено
			return mid
		if guess > item:#Много
			high = mid - 1
		else:#Мало
			low = mid + 1
	return None#Значение не существует
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]#А теперь протестируем функцию!

print(binary_search(my_list, 3))# => 1 Вспомните: нумерация элементов начинается с 0. Второй ячейке соответствует индекс 1
print(binary_search(my_list, -1))# => None "None" в Python означает "нечего". Это призрак того, что элемент не найден
print(binary_search(my_list, 7))
# Сортировка Пузырькои
nums = [2,5,1,8,7,3,4,6,9]

print(nums)

swaps = True
while swaps:
	swaps = False

for i in range(len(nums)):
	for j in range(len(nums)-i-1):
		if nums[j] > nums[j+1]:
			swaps = True
			nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

#Вычисление Факториала Числа
number = 5

def factorial(n):
	if n == 0:
		return 1
	f = 1
	i = 0
	while i < n:
		i += 1
		f = f * 1

#Числа Фибоначи
f1 = f2 = 1
n = 10

print(f1, end=' ')
print(f2, end=' ')

for i in range(2, n):
	f1, f2 = f2, f1 + f2 #Сумма двух
	#Предыдущих чисел
	print(f2, end=' ')

#Выводим конкретный ряд
print(f2)

def fib():
	f1, f2 = 0, 1

	while True:
		yield f1
		f1, f2 = f2, f1 + f2

for i, f in zip(range(10+1), fib()):
	print("{i:3}: {f:3}".format(i=i, f=f))

print("Факториал числа {n} равен {f}".format(n=number, f=factorial(number)))

class Yura:
	pass #Пустой блок

y = Yura()
print(y)

class HaiTec:
	def sayHi(self):
		print('О Здарова, а я, не ждал вас')

h = HaiTec()
h.sayHi()

class Geronimo:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Что же пора', self.name)

g = Geronimo('Прыгать вниз')
g.say_hi()

class Robot:
	'''Представляет робота с именем.'''
	# Переменная класса, содержащая количество роботов
	population = 0
	def __init__(self, name):
		'''Инициализация данных.'''
		self.name = name
		print('(Инициализация {0})'.format(self.name))
		# При создании этой личности, робот добавляется
		# к переменной 'population'
		Robot.population += 1
	def __del__(self):
		'''Я умираю.'''
		print('{0} уничтожается!'.format(self.name))
		Robot.population -= 1
		if Robot.population == 0:
			print('{0} был последним.'.format(self.name))
		else:
			print('Осталось {0:d} работающих роботов.'.format( \
																Robot.population))
	def sayHi(self):
		'''Приветствие робота.
			Да, они это могут.'''
		print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
	def howMany():
		'''Выводит численность роботов.'''
		print('У нас {0:d} роботов.'.format(Robot.population))
	howMany = staticmethod(howMany)

droid1 = Robot('Pixel_0.1')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('Chip_0.1')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()

@staticmethod
def howMany():
	print('У нас {0:d} роботов.'.format(Robot.population))

class SchoolMember:
	'''Представляет любого человека в школе.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Создан SchoolMember: {0})'.format(self.name))
	def tell(self):
		'''Вывести информацию.'''
		print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
	'''Представляет преподавателя.'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Создан Teacher: {0})'.format(self.name))
	def tell(self):
		SchoolMember.tell(self)
		print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
	'''Представляет студента.'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Создан Student: {0})'.format(self.name))
	def tell(self):
		SchoolMember.tell(self)
		print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print() # печатает пустую строку

members = [t, s]
for member in members:
	member.tell() # работает как для преподавателя, так и для студента

class Abir(object):
	def __init__(self, **kwargs):
		self.abbrs = kwargs
		self.store = {}
	def __enter__(self):
		for key, value in self.abbrs.iteritems():
			try:
				self.store[key] = globals()[key]
			except KeyError:
				pass
			globals()[key] = value
	def __exit__(self, *args, **kwargs):
		for key in self.abbrs:
			try:
				globals()[key] = self.store[key]
			except KeyError:
				del globals()[key]

print(Abir())

def Smallest(arr):
	smallest = arr[0]#Дпя хранения наименьwеrо значения
	smallest_index = 0#Дпя хранения индекса наименьwеrо значения
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):#Сортирует массив
	newArr = []
	for i in range(len(arr)):
		smallest = Smallest(arr)#Находит наименьший эпемент в массиве и добавnяет ero в новый массив
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5, 3, 6, 2, 10]))

def look_for_key1(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("found the key!")

def look_for_key2(box):
	for item in box:
		if item.is_a_box():
			look_for_key2(item)
		elif item.is_a_key():
			print("fond the key!")

print(look_for_key1, look_for_key2)

def countdown(i):
	print(i)
	if i <= 0:
		return
	else:
		countdown(i-1)

print(countdown(3))

def greet(name):
	print("hello, " + name + "!")
	greet2(name)
	print("getting ready to say bye...")
	print(bye())

print(greet)

def greet2(name):
	print("how are you, " + name + "?")
def bye():
	print("ok bye!", name)

print(greet2)

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)

print(fact(5))

def sum(arr):
	total = 0
	for x in arr:
		total += x
	return total

print(sum([1, 2, 3, 4]))

def sum(list):
	if list == []:
		return 0
	return list[0] + sum(list[1:])

def count(list):
	if list == []:
		return 0
	return 1 + count(list[1:])

def max(list):
	if len(list) == 2:
		return list[0] if list[0] > list[1] else list[1]
	sub_max = max(list[1:])
	return list if list[0] > sub_max else sub_max

print(sum([33, 15, 7]), ',', count([33, 15, 7]))
print(max([1, 2, 3, 4]))

def quick_sort(array):
	if len(array) < 2:
		return array

print(quick_sort([15, 10, 33]))

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i > pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

def print_items(list):
	for item in list:
		print(item)

print(print_items([2, 4, 6, 8, 10]))

from time import sleep
def print_items2(list):
	for item in list:
		sleep(1)
		print(item)

print(print_items2([2, 4, 6, 8, 10]))

import Maggie

phone_book = {}
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911
print(phone_book["jenny"])

voted = {}
def check_voter(name):
	if voted.get(name):
		print("kick them out!")
	else:
		voted[name] = True
		print("let them vote!")

print(check_voter("tom"))
print(check_voter("mike"))
print(check_voter("mike"))

cache = {}
def get_page(url):
	if cache.get(url):
		return cache[url]
	else:
		data = get_data_from_server(url)
		cache[url] = data
		return data

print(get_page)

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
print(graph)

def person_is_seller(name):
	return name[-1] == 'm'

from collections import deque
def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + "is a mango seller!")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False
search("you")

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

print(graph["start"]["a"], graph["start"]["b"])

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}#У конечного уэла нет соседей

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

processed = [parents, costs, infinity, graph]
node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

print(find_lowest_cost_node)

def groupbyUnsorted(input, key=lambda x:x):
	yielded = set()
	keys = [key(element) for element in input]
	for i, wantedKey in enumerate(keys):
		if wantedKey not in yielded:
			yield (wantedKey(input[j] for j in range(i, len(input)) if keys[j] == wantedKey))
		yielded.add(wantedKey)

xs = [
	[1,2,3,4],
	[5,6,7,8],
	[9,0,0,1],
	[2,3],
	[0],
	[5,8,3,2,5,1],
	[6,4],
	[1,6,9,9,2,9]
]

print(groupbyUnsorted(xs))

for an_int in range(0, 256 + 1):
	print(an_int, "takes", an_int.bit_length(), "bits to represent,")
	print("and equals", bin(an_int), "in binary")

arr = [1, 2, 2, 3, 3, 3]
print(set(arr))

fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])
print(fruits | vegetables, "\n", fruits & vegetables, "\n", fruits - vegetables, "\n", vegetables - fruits)

import itertools

def retry(delays=(0, 1, 5, 30, 180), exception=Exception, report=lambda *args: None):
	def wrapper(function):
		def wrapped(*args, **kwargs):
			problems = []
			for delay in itertools.chain(delays[None]):
				try:
					return function(*args, **kwargs)
				except exception as problem:
					problems.append(problem)
					if delay is None:
						report("retryable failed definitely:", problems)
						raise
					else:
						report("retryable failed definitely:", problems, "-- delaying for %ds" % delay)
						time.sleep(delay)
		return wrapped
	return wrapper

print(retry())

import sys

echo=sys.stdout.write

newline="\n"
char="!"
num=1
strng1="Python Version"
strng2=".4.0 for the AMIGA to 3.5.x"

echo("This works from %s%u%s on any platform%c%c" %(strng1, num, strng2, char, newline))

import inspect
# Define несколько функций с возрастающей арностью:

def f0():
	pass
def f1(a1):
	pass
def f2(a1, a2):
	pass
def f3(a1, a2, a3):
	pass
def f4(a1, a2, a3, a4):
	pass
def main():
	# Определите несколько нефункциональных объектов:
	int1 = 0
	float1 = 0.0
	str1 = ''
	tup1 = ()
	lis1 = []
	for o in (f0, f1, f2, f3, f4, int1, float1, str1, tup1, lis1):
		if not inspect.isfunction(o):
			print(repr(0), 'is not a function')
			continue
		n_args = len(inspect.getargspec(o)[0])
		if n_args == 0:
			num_suffix = '(no) args'
		elif n_args == 1:
			num_suffix = 'arg'
		else:
			num_suffix = 'args'
		print(o.__name__, 'is a function that takes', n_args, num_suffix)

if __name__ == '__main__':
	main()

for x in [1, 2, 3]:
	print(x)

arr1 = [1, 2, 3, 4, 5]
arr2 = map(lambda x: 2 * x, arr1)
print(arr1)

import os
print(os.system('time 0:10'))

from math import *
from functools import wraps

def autocast(method):
	@wraps(method)
	def wrapper(self, obj):
		try:
			return method(self, self.__class__(*obj))
		except TypeError:
			return method(Self, obj)
	return wrapper

for value in (None, "Hi!"):
	try:
		print("Attempting to convert", value, "-->")
		print(float(value))
	except (TypeError, ValueError):
		print("Something went wrong!")
for value in (None, "Hi!"):
	try:
		print("Attempting to convert", value, "-->")
		print(float(value))
	except TypeError:
		print("I can only converta string or a number!")
	except ValueError:
		print("I can only convert a string of digits!")

try:
	from functools import reduce
except:
	pass

data = {
	'des_system_lib':   set('std synopsys std_cell_lib des_system_lib dw02 dw01 ramlib ieee'.split()),
	'dw01':             set('ieee dw01 dware gtech'.split()),
	'dw02':             set('ieee dw02 dware'.split()),
	'dw03':             set('std synopsys dware dw03 dw02 dw01 ieee gtech'.split()),
	'dw04':             set('dw04 ieee dw01 dware gtech'.split()),
	'dw05':             set('dw05 ieee dware'.split()),
	'dw06':             set('dw06 ieee dware'.split()),
	'dw07':             set('ieee dware'.split()),
	'dware':            set('ieee dware'.split()),
	'gtech':            set('ieee gtech'.split()),
	'ramlib':           set('std ieee'.split()),
	'std_cell_lib':     set('ieee std_cell_lib'.split()),
	'synopsys':         set(),
	}

def toposort2(data):
	for k, v in data.items():
		v.discard(k) # Ignore self dependencies
	extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
	data.update({item:set() for item in extra_items_in_deps})
	while True:
		ordered = set(item for item,dep in data.items() if not dep)
		if not ordered:
			break
		yield ' '.join(sorted(ordered))
		data = {item: (dep - ordered) for item,dep in data.items()
				if item not in ordered}
	assert not data, "A cyclic dependency exists amongst %r" % data

print('\n'.join(toposort2(data)))

class L(list):
	def __new__(self, *args, **kwargs):
		return super(L, self).__new__(self, args, kwargs)
	def __init__(self, *args, **kwargs):
		if len(args) == 1 and hasattr(args[0], '__iter__'):
			list.__init__(self, args[0])
		else:
			list.__init__(self, args)
		self.__dict__.update(kwargs)
	def __call__(self, **kwargs):
		self.__dict__.update(kwargs)
		return self

a = L(1, 2, 4, 8)
a2 = L(1, 2, 4, 8, x="Hey!")
a3 = L(1, 2, 4, 8 )( x="Hey!")
a4 = L([1, 2, 4, 8] , x="Hey!")
a5 = L({1, 2, 4, 8} , x="Hey!")
a6 = L([2 ** b for b in range(4)] , x="Hey!")
a7 = L((2 ** b for b in range(4)) , x="Hey!")
a8 = L(2 ** b for b in range(4))( x="Hey!")
a9 = L(2)
print(a)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)
print(a9)
print(len(a))
a.x = "Hey!"
print(a.x)

d = [1000]
f = [3, 5, 6, 9]

d = list(f)
print(d)

e=[1,2,3,5,6,7,8,9]
def binary_searche(e, key, start, end):
	if start <= end:
		mid=int((start+end)/2)
		if key>a[mid]:
			return mid+1
		elif key<a[mid]:
			return mid-1
		else:
			return mid
print(binary_searche(e,3,5,len(a)-1))

print(0x01, 0x10, 0xFF)

def deri():
	coeff=eval(input("Enter the coefficient assuming there is one: "))
	exp=eval(input("Enter the exponent of the coefficient: "))
	if coeff<0 and exp<0:
		print("The derivative is: ", abs(coeff*exp), "/(x^", abs((exp-1)), ")")
	elif exp>1:
		print("The derivative is: ", coeff*exp, "x^", exp-1)
	elif exp==1:
		print("The derivative is: ", coeff)
	elif exp==0:
		print("The derivative is: 0")
	elif coeff<0:
		print("The derivative is: ", coeff*exp, "x^", exp-1)
	elif coeff==0:
		print("The derivative is: 0")
	elif exp<0:
		print("The derivative is: ", coeff*exp, "/(x^", abs(exp-1), ")")
print(deri())

# Счастливых праздников!
# с высотой = 5:
#     *
#    ***
#   *****
#  *******
# *********
#     |

height = 5
stars = 1
for i in range(height):
	print((' ' * (height - i)) + ('*' * stars))
	stars += 2
print((' ' * height) + '|')

class easyaccessdict(dict):
	def __getattr__(self, name):
		if name in self:
			return self[name]
		n=easyaccessdict()
		super().__setitem__(name, n)
		return n
	def __getitem__(self, name):
		if name not in self:
			super().__setitem__(name, nicedict())
		return super().__getitem__(name)
	def __setattr__(self, name, value):
		super().__setitem__(name, value)

d = easyaccessdict()
d.foo.bar = 'a'
d['foo'].blah = 7
d.a.b.c.e.e.f.g.h = 11
print(d)
print(d['foo'])
print(d)
print(d)
print(d)

import heapq

class Heap(list):
	def __init__(self, * pos_arg, ** nam_arg):
		list.__init__(self, * pos_arg, ** nam_arg)
	def pop(self):
		return heapq.heappop(self)
	def push(self, item):
		heapq.heappush(self, item)
	def pushpop(self, item):
		return heapq.heappushpop(self, item)
	def poppush(self, itemp):
		return heapq.replace(self, item)

print(Heap())

"""
	@author   Thomas Lehmann
	@file     four_cubes_problem.py

	There are four cubes with concrete colors on their sides and the goal
	is to place each cube in one row that way, that along the row each side
	presents four different colors:

	 -   -   -   -
	|W| |R| |G| |B| (front view)
	 -   -   -   -

	Of course four different colors are also required at the top view
	at the bottom view and at the back view.

	Background: I have those four cubes in real and I have been seeking
				for the solution without manual try.

"""
import random

class Color:
	""" represents a kind of enum for all used colors """
	GREEN = 0
	RED   = 1
	WHITE = 2
	BLUE  = 3

	MAX   = 4

	@staticmethod
	def name(value):
		return ["GREEN", "RED", "WHITE", "BLUE"][value]

class Cube:
	def __init__(self, front, back, left, right, top, bottom):
		""" initializes all sides of a cube with colors """
		self.front  = front
		self.back   = back
		self.left   = left
		self.right  = right
		self.top    = top
		self.bottom = bottom

	def __eq__(self, other):
		""" compares this cube and another for to be equal """
		return self.front   == other.front  \
			and self.back   == other.back   \
			and self.left   == other.left   \
			and self.right  == other.right  \
			and self.top    == other.top    \
			and self.bottom == other.bottom

	def __hash__(self):
		""" unique key for this instance """
		return hash((self.front, self.back, self.left, self.right, self.top, self.bottom))

	def clone(self):
		""" provides a copy of this instance """
		return Cube(self.front, self.back, self.left, self.right, self.top, self.bottom)

	def __str__(self):
		""" does print the current cube setup (colors) """
		return "front:"  + Color.name(self.front)  + "," + \
			   "back:"   + Color.name(self.back)   + "," + \
			   "left:"   + Color.name(self.left)   + "," + \
			   "right:"  + Color.name(self.right)  + "," + \
			   "top:"    + Color.name(self.top)    + "," + \
			   "bottom:" + Color.name(self.bottom)

	def getCombinations(self):
		""" I know: there should be 24 combinations """
		cubes = set()
		cubes.add(self.clone())

		cube = self.clone()
		while not len(cubes) == 24:
			mode = random.randint (0, 4)
			if   0 == mode:  cube.rotateLeft()
			elif 1 == mode:  cube.rotateRight()
			elif 2 == mode:  cube.rotateTop()
			elif 3 == mode:  cube.rotateBottom()
			cubes.add(cube.clone())

		return cubes

	def rotateLeft(self):
		""" does rotate the cube to the left """
		help       = self.left
		self.left  = self.front
		self.front = self.right
		self.right = self.back
		self.back  = help
		return self

	def rotateRight(self):
		""" does rotate the cube to the right """
		help       = self.right
		self.right = self.front
		self.front = self.left
		self.left  = self.back
		self.back  = help
		return self

	def rotateTop(self):
		""" does rotate the cube to the top """
		help        = self.top
		self.top    = self.front
		self.front  = self.bottom
		self.bottom = self.back
		self.back   = help
		return self

	def rotateBottom(self):
		""" does rotate the cube to the bottom """
		help        = self.bottom
		self.bottom = self.front
		self.front  = self.top
		self.top    = self.back
		self.back   = help
		return self

class CubesChecker:
	def __init__(self, cubes):
		self.originalCubes = cubes

	@staticmethod
	def isValidState(cubes):
		""" ensure the rule: four different colors on each side """
		frontColors  = set()
		backColors   = set()
		topColors    = set()
		bottomColors = set()

		for cube in cubes:
			frontColors.add(cube.front)
			backColors.add(cube.back)
			topColors.add(cube.top)
			bottomColors.add(cube.bottom)

		return  len(frontColors)  == Color.MAX \
			and len(backColors)   == Color.MAX \
			and len(topColors)    == Color.MAX \
			and len(bottomColors) == Color.MAX

	def calculate(self, position = 0, cubes = []):
		""" find the cubes final state """
		if len(cubes) == Color.MAX:
			if CubesChecker.isValidState(cubes):
				for cube in cubes:
					print(cube)
				return True
			else:
				return False

		for cube in self.originalCubes[position].getCombinations():
			if self.calculate(position+1, cubes + [cube]):
				return True

		return False

def main():
	""" there are four cubes with concrete colors on their sides and the goal
		is to place each cube in one row that way that along the row each side
		presents four different colors """
	#              -----------  -----------  -----------  -----------  -----------  -----------
	#              front        back         left         right        top          bottom
	#              -----------  -----------  -----------  -----------  -----------  -----------
	cubes = [ Cube(Color.GREEN, Color.WHITE, Color.GREEN, Color.RED,   Color.WHITE, Color.BLUE),
			  Cube(Color.WHITE, Color.RED  , Color.WHITE, Color.GREEN, Color.BLUE,  Color.RED),
			  Cube(Color.RED,   Color.RED,   Color.RED  , Color.GREEN, Color.BLUE,  Color.WHITE),
			  Cube(Color.BLUE,  Color.RED,   Color.GREEN, Color.GREEN, Color.WHITE, Color.BLUE) ]

	cubesChecker = CubesChecker(cubes)
	cubesChecker.calculate()

if __name__ == "__main__":
	main()

class MyClass:
	i = 12345
	def f(self):
		return 'hello world'
x = MyClass()
print(x)

import random
print(random.choice(['apple', 'pear', 'banana']))

name = input("Hi, what's your name?: ")
print(name)
print("Hi, " + name)

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

c=input("Ввидите число, чтобы создать ципочка ДНК: ")
if len(c)>1:
	c=c[0]
if len(c)<1:
	c='#'
Turns=4
s=" "
def bids(a,b,c="",d=""):
	return(a+b+c+d)
def strand():
	print(bids(s*19,c))
	print(bids(s*17,c*4))
	print(bids(s*16,c*6))
	print(bids(s*14,c*2,s*6,c*2))
	print(bids(s*12,c*14))
	print(bids(s*11,c*2,s*12,c*2))
	print(bids(s*11,c*16))
	print(bids(s*12,c*2,s*10,c*2))
	print(bids(s*14,c*10))
	print(bids(s*16,c*2,s*2,c*2))
	print(bids(s*17,c*4))
	print(bids(s*18,c*2))

for i in range(Turns):
	strand()
print(" ")
print("First Python Code!please leave a like")

import os
import struct

def random_1():
	return (int.from_bytes(os.urandom(7), "big") >> 3) * 2 ** -53
def random_2():
	return (int.from_bytes(os.urandom(7), 'big') >> 3) / (1 << 53)
def random_3():
	array = bytearray('b\x3F' + os.urandom(7))
	array[1] |= 0xF0
	return struct.unpack('>d', array)[0] - 1

states = {
		'AK': 'O',
		'AL': 'S',
		'AR': 'S',
		'AS': 'O',
		'AZ': 'W',
		'CA': 'W',
		'CO': 'W',
		'CT': 'N',
		'DC': 'N',
		'DE': 'N',
		'FL': 'S',
		'GA': 'S',
		'GU': 'O',
		'HI': 'O',
		'IA': 'M',
		'ID': 'W',
		'IL': 'M',
		'IN': 'M',
		'KS': 'M',
		'KY': 'S',
		'LA': 'S',
		'MA': 'N',
		'MD': 'N',
		'ME': 'N',
		'MI': 'W',
		'MN': 'M',
		'MO': 'M',
		'MP': 'O',
		'MS': 'S',
		'MT': 'W',
		'NA': 'O',
		'NC': 'S',
		'ND': 'M',
		'NE': 'W',
		'NH': 'N',
		'NJ': 'N',
		'NM': 'W',
		'NV': 'W',
		'NY': 'N',
		'OH': 'M',
		'OK': 'S',
		'OR': 'W',
		'PA': 'N',
		'PR': 'O',
		'RI': 'N',
		'SC': 'S',
		'SD': 'M',
		'TN': 'S',
		'TX': 'S',
		'UT': 'W',
		'VA': 'S',
		'VI': 'O',
		'VT': 'N',
		'WA': 'W',
		'WI': 'M',
		'WV': 'S',
		'WY': 'W'
}
print(states)

n = int(input("Введите число: "))
m = n//2
for x in range(1,n + 1,2):
	print(' '*m + '*'*x)
	m=m-1

import contextlib
import os
import stat
import sys
import tempfile

@contextlib.contextmanager
def atomic_write(filename, text=True, keep=True, owner=None, group=None, perms=None, suffix='.bak', prefix='tmp'):
	t = (uid, gid, mod) = (owner, group, perms)
	if any(x is None for x in t):
		info = os.stat(filename)
		if uid is None:
			uid = info.st_uid
		if gid is None:
			gid = info.st_gid
		if mod is None:
			mod =  stat.S_IMODE(info.st_mode)
	path = os.path.dirname(filename)
	fd, tmp = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=path, text=text)
	try:
		replace = os.replace
	except AttributeError:
		if sys.platform == 'win32':
			def replace(source, destination):
				assert sys.platform == 'win32'
				try:
					os.rename(source, dest)
				except OSError as err:
					if err.winerr != 183:
						raise
					os.remove(dest)
					os.rename(source, dest)
		else:
			replace = os.raname
	try:
		with os.fdopen(fd, 'w' if text else 'wb') as f:
			yield f
		replace(tmp. filename)
		tmp = None
		os.chown(filename, uid, gid)
		os.chmod(filename, mod)
	finally:
		if (tmp is not None) and (not keep):
			try:
				os.unlink(tmp)
			except:
				pass

from decimal import Decimal

def eng(num):
	return Decimal(num).normalize().to_eng_string()
if __name__ == '__main__':
	TTT = [-78951, -500, 1e-3, 0.005, 0.05, 0.12,
			   10, 23.3456789, 50, 150, 250, 800, 1250,
			   127e11, 51234562]
	for x in TTT:
		print("%s: %s " % (x, eng(x)))

class _Getch:
	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError:
			self.impl = _GetchUnix()
	def __call__(self):
		return self.impl()
class _GetchUnix:
	def __init__(self):
		import tty, sys
		from select import select
	def __call__(self):
		import sys, tty, termios
		from select import select
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			[i, o, e] = select([sys.stdin.fileno()], [], [], 1)
			if i:
				ch = sys.stdin.read(1)
			else:
				ch = None
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
class _GetchWindows:
	def __init__(self):
		import msvcrt
	def __call__(self):
		import msvcrt
		import time
		time.sleep(1)
		if msvcrt.kbhit():
			return msvcrt.getch()
		else:
			return
getch = _Getch()
print(getch())

import os

for k, v in os.environ.items():
	print("%s=%s" % (k,v))
print("\n".join(["%s=%s" % (k, v) for k, v in os.environ.items()]))

from math import sqrt

for n in range(99, 0, -1):
	root = sqrt(n)
	if root == int(root):
		print(n)
		break

print(min(9, 3, 2, 5))

numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))

def func(x, y, z):
	return x + y + z
print(func, (2,3,4))
f = lambda x, y, z:x + y + z
print(func, f(2, 3, 4))

try:
	num = float(input("\nEnter a number: "))
except(ValueError):
	print("That was not a number!")

integer1 = 9
integer2 = 2

sum = integer1 + integer2
print("sum: ", id(sum), type(sum), sum)

nums = range(2, 50)
for i in range(2, 8):
	nums = filter(lambda x: x == i or x % i, nums)
print(nums)

def f(x):
	return x % 2 != 0 and x % 3 != 0
print(filter(f, range(2, 25)))

print(filter((lambda x: x > 0), range(-5, 5)))

import sys

def printList(alist):
	print(''.join(alist))
def printUniqueCombinations(alist, numb, blist=[]):
	if not numb: return printList(blist)
	for i in range(len(alist)):
		blist.append(alist[i])
		printUniqueCombinations(alist[i+1:], numb-1, blist)
		blist.pop()
def printCombinations(alist, numb, blist=[]):
	if not numb: return printList(blist)
	for i in range(len(alist)):
		blist.append(alist.pop(i))
		printCombinations(alist, num-1, blist)
		alist.insert(i, blist.pop())
if __name__ == '__main__':
	k='Dead'
	n=2
	if len(sys.argv)>= 2: k = sys.argv[1]
	if len(sys.argv)>=3: n = int(sys.argv[2])
	print('combinations of %d letters in "%s" ' % (n, k))
	printCombinations(list(k), n)
	print('unique combinations of %d letters in "%s" ' % (n, k))
	printUniqueCombinations(list(k), n)

class RingBuffer:
	def __init__(self, size_max):
		self.max = size_max
		self.data = []
	def append(self, x):
		self.data.append(x)
		if len(self.data) == self.max:
			self.cur = 0
			self.__class__ = RingBufferFull
	def get(self):
		return self.data
class RingBufferFull:
	def __init__(self, n):
		raise "you should use RingBuffer"
	def append(self, x):
		self.data[self.cur] = x
		self.cur = (self.cur+1) % self.max
	def get(self):
		return self.data[self.cur:]+self.data[:self.cur]
x = RingBuffer(5)
x.append(1); x.append(2); x.append(3); x.append(4)
print(x.__class__,x.get())
x.append(5)
print(x.__class__,x.get())
x.append(6)
print(x.data,x.get())
x.append(7); x.append(8); x.append(9); x.append(10)
print(x.data, x.get())

def decode(*arguments):
	if len(arguments) < 3:
		raise TypeError + 'decode() takes at least 3 arguments (%d given)' % (len(arguments))
	dict = list(arguments[1:])
	if arguments[0] in dict:
		index = dict.index(arguments[0]);
		if index % 2 == 0 and len(dict) > index+1:
			return dict[index+1]
		return dict[-1]
	elif len(dict) % 2 != 0:
		return dict[-1]
return_value = decode('b', 'a', 1, 'b', 2, 3)
var = 'list'
return_type = decode(var, 'tuple', (), 'dict', {}, 'list', [], 'string', '')
print(return_type)

def binary_search(seq, t):
	min = 0
	max = len(seq) - 1
	while True:
		if max < min:
			return -1
		m = (min + max) // 2
		if seq[m] < t:
			min = m + 1
		elif seq[m] > t:
			max = m - 1
		else:
			return m

def prune(L, unique_items):
	map(L.remove, unique_items)
def graft(L, unique_items):
	L.extend(unique_items)
def unique(L1, L2):
	return [item for item in L1 if item not in L2]
if __name__ == "__main__":
	list1 = ["a", "b", "c", "e", "f", "d"]
	list2 = ["a", "b", "f", "g"]
	prune(list1, unique(list1, list2))
	graft(list1, unique(list2, list1))
	print("list1 =", list1)
	print("list2 =", list2)

import os
print(os.system('time 0:02'))

def oa(o):
	for at in dir(o):
		print(at, oa({}), oa([]), oa(1))
def oar(o):
	for at in dir(o):
		if not at.startswith('__') and not at.endswith('__'):
			print(at, oar({}), oar(1), oar(''))

import os, sys
print('my os.getcwd =>', os.getcwd())
print('my sys.path =>', sys.path[:6])

print("107 % 4 = ", 104 % 4)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(lambda x: x % 3 == 0, foo))

nums = range(2, 50)
for i in range(2, 8):
	nums = filter(lambda x: x == i or x % i, nums)
print(nums)

from colorama import init
from colorama import Fore, Style, Back
init(autoreset=True)

n = Fore.BLUE +"Yura" * 100
e = Fore.YELLOW + "Isaac" * 100
t = Fore.GREEN + "DoctorKek" * 100
i = Fore.RED + "Muchin" * 100
print(n, e, t, i)

import math

ratio = math.pi.as_integer_ratio()
print(ratio[0] / ratio[1])
print(1.0 * ratio[0] / ratio[1])

class IllegalCharacterError(Exception):
    pass

def romanToNumber(numerals):
    '''Converts a string of Roman Numerals (I,V,X,L,C,D,M) into an integer.'''

    romanConversionTable = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    ### Build List of Numbers ###
    
    numberList = []
    for letter in numerals:
        # Build List of Numbers
        if letter in romanConversionTable:
            numberList += [romanConversionTable[letter]]
        else:
            raise IllegalCharacterError('{} is not a Roman Numeral'.format(letter))

    if len(numberList) == 1:
        return numberList[0]

    ### Construct Final Total ###

    previous = numberList[-1]
    total = previous
    for current in range(len(numberList)-2,-1, -1):
        if numberList[current] < previous:
            total -= numberList[current]
        else:
            total += numberList[current]
        previous = numberList[current]

    return total

def numberToRoman(integer):
    '''Converts an integer into a string of Roman Numerals.'''

    if type(integer) != int:
        raise TypeError('Input must be an integer.')
    
    numberConversionTable = {
        1 : 'I',
        5 : 'V',
        10 : 'X',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        1000 : 'M'
    }
    quads = ('I','X','C')
    doubs = ('V','L','D')
    foundNumeral = ''
    found = 0

    ### Build List of Roman Numerals ###

    numeralList = []
    for value in [1000,500,100,50,10,5,1]:
        while integer >= value:
            integer -= value
            numeralList += [numberConversionTable[value]]
    if len(numeralList) == 1: #Return result if only one symbol
        return numeralList.pop()

    ### Modify List to Proper Formatting ###

    finalNumeralList = []
    repeats = 0

    for numeral in numeralList:
        if len(finalNumeralList) == 0:
            # ADD FIRST NUMBER
            finalNumeralList += [numeral]
        else:
            if numeral != finalNumeralList[len(finalNumeralList)-1]:
                # CURRENT NUMERAL IS DIFFERENT FROM THE LAST
                if 3 > repeats > 0:
                    # ADD IN ALL REPEATS
                    for i in range(repeats):
                        finalNumeralList += [finalNumeralList[-1]]
                repeats = 0
                finalNumeralList += [numeral]
            else:
                # CURRENT NUMERAL IS THE SAME AS THE LAST
                repeats += 1
                if repeats == 3 and numeral != 'M':
                    # EXCHANGE THREE ONES NUMERALS FOR ONE FIVES NUMERAL
                    modifiedNumeral = doubs[quads.index(numeral)]
                    if modifiedNumeral == finalNumeralList[len(finalNumeralList)-2]:
                        # NUMERALS IN A THREE DIGIT RANGE ADD TO 9
                        finalNumeralList.pop(len(finalNumeralList)-2)
                        if numeral != 'C':
                            finalNumeralList += [quads[quads.index(numeral)+1]]
                        else:
                            finalNumeralList += ['M']
                    else:
                        finalNumeralList += [modifiedNumeral]
                    repeats = 0
                elif numeral == 'M':
                    # AUTOMATICALLY ADD M
                    finalNumeralList += ['M']
                    repeats = 0
                    
    if repeats > 0:
        # ADD IN ANY REMAINING REPEATS
        for i in range(repeats):
            finalNumeralList += [finalNumeralList[-1]]
                        
    finalString = ''.join(finalNumeralList)
                                                        
    return finalString

print(IllegalCharacterError(2))

class Prod:
	def __init__(self, value):
		self.value = value
	def __call__(self, other):
		return self.value * other
x = Prod(2)
print(x(3))
print(x(4))

a = ['spam', 'eggs', 100, 1234]
print(a)

def convert_slice_to_list(Slice, list_length):
	return list(range(list_length))[Slice]
class poor_man_1D_mgrid:
	def __getitem__(self, s):
		try:
			start, stop, step = s.start, s.stop, s.step
		except:
			raise TypeError('expected a slice')
		start = start or 0
		step = step or 1
		L = stop - start
		if isinstance(step, complex):
			intervals = max(int(0.5+abs(step)), 2)
			step = L/(intervals-1)
			halfway = start+L/2
			l,r = [],[]
			for i in range(int(intervals/2)):
				delta = step*i
				r.append(stop - delta)
				l.append(start + delta)
			if intervals & 1:
				l.append(l[-1]+(r[-1]-l[-1])/2)
			l.extend(reversed(r))
			return l
		if (L < 0) and (step == 1):
			step = -1
		if step*L < 0:
			raise ValueError('avoid infinite list')
		return [start+step*i for i in range(max(int(0.5+L/step), 1))]
mgrid = poor_man_1D_mgrid()
print(mgrid)

inventory = ()
if not inventory:
	print("You are empty-handed")

l = "Isaac_Muchin"
print(l[::-1])

from collections import Counter

if (Counter("RIP") == Counter("BIP")):
	print("Это анаграмма!")

i = "assassin fig suck"
print(i.title())

o = "PyThOn"
print(o.lower(), o.upper())

r = "SCELETONS"
print(list(r))

from collections import Counter
numbum2 = [1,2,3,3,3,4,5,6,6]
def most_common(list):
	data = Counter(list)
	return data.most_common(1)[0][0]
print(most_common(numbum2))

h = [1,2,3,3]
if(len(h) == len(set(h))):
	print("Список уникальный")
else:
	print("Список НЕ уникальный")

p = [1,2,3,3]
print(set(p))

gg = [0,1,2,3,'',False,'a','b','c']
print(list(filter(bool, gg)))

def diff(list1, list2):
	return list(set(list1).symmetric_difference(list2))
a = [1,2,3]
b = [1,2,3,4]
print(diff(a, b))

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
print(sys.getrecursionlimit)

d = {'url': 'http://www.python.org', 'spam':0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)

def of_bucket(lst, depth=0):
	for item in lst[0]:
		if len(lst) > 1:
			for result in of_bucket(lst[1:], depth+1):
				yield [item,] + result
		else:
			yield [item,]
if __name__ == '__main__':
	bucket_lst = [["ba", "be", "bi"], ["ka", "ko", "ku", "ke"], ["to", "ty"]]
	for n, combination in enumerate(of_bucket(bucket_lst)):
		print("{0:2d}. {1}".format(n, '-'.join(combination)))

d = {}
print(d.setdefault('name', 'N/A'))
print(d)
d['name'] = 'Gumby'
d.setdefault('name','N/A')
print(d)
d = {}
print(d.setdefault('name'))
print(d)

def scriptinfo():
	import os, sys, inspect
	for teil in inspect.stack():
		if teil[1].startswith("<"):
			continue
		if teil[1].upper().startswith(sys.exc_prefix.upper()):
			continue
		trc = teil[1]
	if getattr(sys, 'frozen', False):
		scriptdir, scriptname = os.path.split(sys.executable)
		return {"dir": scriptdir, "name": scriptname, "source": trc}
	scriptdir, trc = os.path.split(trc)
	if not scriptdir:
		scriptdir = os.getcwd()
	scr_dict = {"name": trc, "source": trc, "dir": scriptdir}
	return scr_dict

from numba import jit
import random
@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
print(monte_carlo_pi(60))

print(eval('100'), eval('0x40'))

import heapq

class Heap(list):
	def __init__(self, *pos_arg, **nam_arg):
		list.__init__(self, *pos_arg, **nam_arg)
	def pop(self):
		return heapq.heappop(self)
	def push(self, item):
		heapq.heappush(self, item)
	def pushpop(self, item):
		return heapq.heappushpop(self, item)
	def poppush(self, itemp):
		return heapq.replace(self, item)

print(Heap())

def polignac(num, p):
	factorsDict = {}
	if num>1 and p==1:
		print("Invalid entry since 1 is the identity.")
	else:
		while num>1:
			factorsDict[num//p]=num//p
			num=num//p
		return sum(factorsDict)

def extendedEuclid(a, b):
	b,a = max(a,b), min(a,b)
	euclidList=[[b%a, 1, b, -1*(b//a), a]]
	while b%a>0:
		b,a=a,b%a
		euclidList.append([b%a, 1, b, -1*(b//a), a])
	if len(euclidList)>1:
		euclidList.pop()
		euclidList=euclidList[::-1]
		for i in range(1, len(euclidList)):
			euclidList[i][1]*=euclidList[i-1][3]
			euclidList[i][3]*=euclidList[i-1][3]
			euclidList[i][3]*=euclidList[i-1][1]
	expr=euclidList[len(euclidList)-1]
	strExpr=str(expr[1])+"*"+str(expr[2])+" + "+str(expr[3])+"*"+str(expr[4])+" = "+str(euclidList[0][0])
	return strExpr

class MyMeta(type):
	def __str__(cls):
		return "Class name is '%s'"%cls.__name__
class MyClass:
	__metaclass__ = MyMeta
x = MyClass()
print(type(x)) 

from psome import psome

def test_psome():
	ls = "This is a list of elements, but not all of them will be printed".split()
	for e in ls:
		psome(e, 6)
if __name__ == '__main__':
	test_psome()

import heapq as hq
inf = float('Inf')
def dijkstra(G, s):
	n = len(G)
	Q = [(0, s)]
	d = [inf for i in range(n)]
	d[s]=0
	while len(Q)!=0:
		(cost, u) = hq.heappop(Q)
		for v in range(n):
			if d[v] > d[u] + G[u][v]:
				d[v] = d[u] + G[u][v]
				hq.heappush(Q, (d[v], v))
	return d
G = [\
        [0.0,  1.0,  3.0,  inf],\
        [1.0,  0.0,  1.0,  4.0],\
        [3.0,  1.0,  0.0,  2.0],\
        [inf,  4.0,  2.0,  0.0]]

d = dijkstra(G, 0)
print(d)

L = [None] * 100
print(L)

li = ['a', 'b', 'new', 'D', 'z', 'example', 'new', 'two', 'elements']
print(li.index("example"))
print(li.index("new"))
print(li.index("z"))
print("c" in li)

def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	return res
x = intersect([1, 2, 3], (1, 4))
print(x)

class SharedData:
	spam = 42
x = SharedData()
y = SharedData()
SharedData.spam = 99
x.spam = 88
print(x.spam, y.spam)
print(x.spam, y.spam, SharedData.spam)
print(x.spam, y.spam, SharedData.spam)

S = "lumberjack"
T = ("and", "I'm", "okay")
for x in S:
	print(x)
for x in T:
	print(x)

integer1 = 9
integer2 = 2
sum = integer1 + integer2
print("sum: ", id (sum), type(sum), sum)

import math
print(math.pi, math.e)
print(abs(-42), 2**4, pow(2, 4))

try:
	num = float(input("\nВведите число: "))
	print(num)
except(ValueError):
	print("Это не было числом!")

fune = (2 + 2)
funi = 5
print(fune / 5)

import collections

class OrderedSet(collections.MutableSet):
	def __init__(self, iterable=None):
		self.end = end = []
		end += [None, end, end]
		self.map = {}
		if iterable is not None:
			self |= iterable
	def __len__(self):
		return len(self.map)
	def __contains__(self, key):
		return key in self.map
	def add(self, key):
		if key not in self.map:
			end = self.end
			curr = end[1]
			curr[2] = end[1] = self.map[key] = [key, curr, end]
	def discard(self, key):
		if key in self.map:
			key, prev, next = self.map.pop(key)
			prev[2] = next
			next[1] = prev
	def __iter__(self):
		end = self.end
		curr = end[2]
		while curr is not end:
			yield curr[0]
			curr = curr[2]
	def __reversed__(self):
		end = self.end
		curr = end[1]
		while curr is not end:
			yield curr[0]
			curr = curr[1]
	def pop(self, last=True):
		if not self:
			raise KeyError('set is empty')
		key = self.end[1][0] if last else self.end[2][0]
		self.discard(key)
		return key
	def __repr__(self):
		if not self:
			return '%s()' % (self.__class__.__name__,)
		return '%s(%r)' % (self.__class__.__name__, list(self))
	def __eq__(self, other):
		if isinstance(other, OrderedSet):
			return len(self) == len(other) and list(self) == list(other)
		return set(self) == set(other)
if __name__ == '__main__':
	s = OrderedSet('abracadaba')
	t = OrderedSet('simsalabim')
	print(s | t)
	print(s & t)
	print(s - t)

quote = "Python is easy to use."
print("Original quote:")
print(quote)
print("\nIn uppercase:")
print(quote.upper())
print("\nOriginal quote is still:")
print(quote)

num = 22
nim = 33
print(num)
nim = num
print(num)

x = 1
x | 2
print(x)

import sys 
def group(a, *ns):
	for n in ns:
		a = [a[i:i+n] for i in xrange(0, len(a), n)]
	return a
def join(a, *cs):
	return [cs[0].join(join(t, *cs[1:])) for t in a] if cs else a
def nexdump(data):
	toHex = lambda c: '{:02X}'.format(ord(c))
	toChr = lambda c: c if 32 <= ord(c) < 127 else '.'
	make = lambda f, *cs: join(group(map(f, data), 8, 2), *cs)
	hs = make(toHex, ' ', ' ')
	cs = make(toChr, ' ', ' ')
	for i, (h, c) in enumerate(zip(hs, cs)):
		print('{:010X}: {:48}  {:16}'.format(i * 16, h, c))

class easyaccessdict(dict):
	def __getattr__(self, name):
		if name in self:
			return self[name]
		n=easyaccessdict()
		super().__setitem__(name, n)
		return n
	def __getitem__(self, name):
		if name not in self:
			super().__setitem__(name, nicedict())
		return super().__getitem__(name)
	def __setattr__(self, name, value):
		super().__setitem__(name, value)
d = easyaccessdict()
d.foo.bar = 'a'
print(d)
print(['foo'])
d['foo'].blah = 7
print(d)
d.a.b.c.e.e.f.g.h= 11
print(d)

import pprint
t = [[['black', 'cyan'], 'white',['green', 'red']], [['magenta', 'yellow'], 'blue']]
print(pprint.pprint(t, width=30))

print("107% 4=")
print(107% 4)

aList = [2, 6, 4, 8, 10, 12, 89, 68, 45, 37]
print("Data items in original order")
for item in aList:
	print(item)
aList.sort()
print("\nData items after sorting")
for item in aList:
	print(item)
print(item)

from collections import defaultdict
from json import dumps

class Hivemind:
	__shared_states = defaultdict(dict)
	def __init__(self, *args, **kwargs):
		key = type(self).__name__, dumps(args, sort_keys = True), dumps(kwargs, sort_keys=True)
		self.__dict__ = self.__shared_states[key]
print(Hivemind())

name=input('\nТвое имя?\n')
print('Уважаемый', name,', наш код заканчивается: ')

print("=====")
print("<#_#>")
print("=====")

print("\nНо вот и всё конец кода")
print("@Yura_Mukhin")
print("{code}, {__version__}: ".format(code='tasks.py', __version__=1.1))
input("Нажмите ENTER: ")