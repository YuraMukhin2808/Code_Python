#Саломалеку Чувачук:)
from __future__ import print_function
from numba import jit 
jit(nopython=True)
from colorama import init
from colorama import Style, Back, Fore
init()
print(Fore.GREEN)
print("Hello user")
print('Привет, меня зовут {name}, и я, написал это код {code} версий {__version__} .'.format(name='Yura Mukhin', code='text.py', __version__=4.0))
print("Добро пожаловать\nв нашу нору\nНо мне нужно знать о тебе по больше")
a = "Пожалуста введите ваше имя"
b = "Введите вашу фамилию"
c = "Введите ваше отечество"
age = "Пожалуста введите ваш возраст"

print( "Привет: " + a +"!")
print( "Можете меня звать: "+ b +"!")
print( "Или: "+ c +"!")
print( "Мне: " + str(age))

a = input("Введите свое имя: ")
b = input("Введите свое фамиля: ")
c = input("Ведите свое отечества: ")
age = input("Укажите свой возраст: ")

print( "Привет, " + a + " !")
print( "Можете звать, " + b + " !")
print( "Или, " + c + " !")
print( "Тебе  " + age + " лет это здорова!!!")

for countodown in 5, 4, 3, 2, 1, "hey!":
    print(countodown)

s = input("Enter something plasse: ")

if 10 >5:
    print("10 grater than 5")

print("Program ended")

print(1 != 1)

print("eleven" != "seven")

nums = [7, 7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [2, 2, 2, 2]
nums[2] = 4
print(nums)

numbers = list(range(10))
print(numbers)

a = 24

b = 13

a = 7
print(a)

b = a
print(b)

a = 95

a = a - 3

temp = a - 3
a = temp

a -= 3

a += 8

a *= 2

a /= 3

a = 13
a //= 4

print(a)

d = lambda p: p * 5
t = lambda p: p * 2
x = 7
x = d(x)
x = t(x)
x = d(x)
print(x)

class change:
    def __init__(self, x, y, z):
        self.a = x + y + z

x = change(1,2,3)
y = getattr(x, 'a')
setattr(x, 'a', y+1)
print(x.a)

def a(b):
    b = b + [5]
c = [1, 2, 3, 4, 5, 6, 7, 8]
a(c)
print(len(c))

x=2019
def f1():
    global x
    x=60
def f2():
    global x
    x=70
print(x)

age = -10

if age in range(0,15):
    print("Child")
elif age in range(15,25):
    print("Youth")
elif age in range(25,65):
    print("Adulf")
else:
    print("Wrong input!") if age<0 else print("Senior")

import builtins
import os
import platform
import random
import sys
import time as t
import urllib.error
import urllib.request
from collections import Counter
from itertools import count

for i in count(20,-3):
    print(i)
    if i < 5:
        break

googol = 10**100
print(googol)

float(True)

float(False)

float('1.0e4')

bottles = 99
base = ''
base += 'current inventory: '
base += str(bottles)
print(base)

print('\tabc')

a = 'Duck.'
b = a
c = 'Grey Duck!'
print(a + b + c)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[3])

nums = [1, 1, 1, 1, 1, 1]
nums[1] = 4
print(nums)

def print_with_exclamation(Hero):
    print(Hero + "!")

print_with_exclamation("Steve")
print_with_exclamation("Alex")
print_with_exclamation("Wolf")

def print_sum_twice(a, b):
    print(a + b)

    print_sum_twice(4, 4)

def rev(n):
    print(n)
    n=n[::-1]
    return int(n)

n=input('Please enter a number of any lengeth: ')
a=rev(n)
print('\nThe reverse of your number is' ,a)

print('\nYour number' ,a, 'pius 56 equals' ,(a+4368))

diceResult1 = 0;
diceResult2 = 0;
roles = 0;

for x in range(200):
    diceResult1 = random.randint(1,6)
    diceResult2 = random.randint(1,6)
    result = diceResult1 + diceResult2
    print("You roll a: " + str(diceResult1) + " and " + str(diceResult2) + " (="+ str(result)+ ")")
    roles+=1
    if(result == 12):
        print("It took " +str(roles)+" dice roles to reach 12.")
        break

a=5
print (a,"is of type",type(a))
a=2,0
print (a,"is of type",type(a))
a=0.00003
print (a,"is of type",type(a))

print("SILVESTR POWER PUNCH IS:")
fighter1=random.randint(1,100)
print(fighter1)
print("LORENS POWER PUNCH IS:")
fighter2=random.randint(1,100)
print(fighter2)
("NOW! FIGHT!!!")
if fighter1>fighter2:
    print("SILVESTR PUNCH IS SO HARD.AND HE WIIINS!!")
elif fighter1<fighter2:
     print("OOW LOURENS WIIINS.HE KICKED IN THE HEAD !!")
elif fighter1==fighter2:
    print("IT'S DROW")

else:
    print("first loop finished normally.")

for i in range(10):
    if i == 5:
        print("2nd loop finished abnormally.")
        break
else:
     print("2nd loop finished normally.")


a = ['array', 'sum', 'tuple', 'range']
b = dir(builtins)

for x in range(len(a)):
    for i in range(len(b)):
        if a[x] == b[i]:
            print('is not', a[x])
        elif a[x] not in b:
            print("it's", a[x])
            break

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'Johh', 'Terry', 'Terry', 'Michael']
another_empty_list = list()
print(another_empty_list)

list('cat')
print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

birthday = '25/09/2019'
print(birthday.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(len(marxes))
print(marxes)

cliches = [
    "At the end of the day",
    "Having said that",
    "The fact of the matter is",
    "Be that as it may",
    "The bottom line is",
    "If you will",
    ]
print(cliches[3])

from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

for stooge in quotes:
    print(stooge)

stooge = "Curly"
print(stooge, "says:", quotes[stooge])

a = [1,2,4,4,5,6,6,6,3,8,0,3,5,9,1,1]

b = Counter(a)
print(b)

print("# of 7s:",b[0])

print("# of 7s:",b[7])

comments_correct = lambda s: s.count('/')%2==0 and s.count('*')%2==0

[print(x,comments_correct(x),sep='\t'*3, end='\n')for x in ['//', '/**///', '/*//*/', '/////**//*//*//*/']]


biome=['island','swamp','rain forest','savannah']

food=['meat','berries','small insect']

island_predator=['snake','coyotes','scorpion']
swamp_predator=['alligator','anaconda','mosquito']
rain_predator=['snake','mosquito','insect']
savannah_predator=['lion','cheetah','snake']

island_shelter=['hut','tree house','small cave']
swamp_shelter=['tree house','small hut','hollow']
rain_shelter=['tree house','hut','cave']
savannah_shelter=['small shelter','small hut']

how_long=['1 day','2 day','3 day','4 day','5 day','6 day','1 week','2 week','3 week','1 month']

biome_choice = random.choice(biome)
food_choice = random.choice(food)
how_long_choice = random.choice(how_long)

if biome_choice == 'island':
    predator_choice = random.choice(island_predator)
    shelter_choice = random.choice(island_shelter)
if biome_choice == 'swamp':
    predator_choice = random.choice(swamp_predator)
    shelter_choice = random.choice(swamp_shelter)
if biome_choice == 'rain forest':
    predator_choice = random.choice(rain_predator)
    shelter_choice = random.choice(rain_shelter)
if biome_choice == 'savannah':
    predator_choice = random.choice(savannah_predator)
    shelter_choice = random.choice(savannah_shelter)
def live():
    live_choice = random.randint(1,4)
    if live_choice == 4:
        print('You did not Survive, Cause of Death: The ' + food_choice + ' was poisionous')
    if live_choice == 3:
        print('You did not Survive, Cause of Death: ' + predator_choice + ' attacked you!')
    if live_choice == 2:
        print('You did not Survive, Cause of Death: Water Pollution')
    if live_choice == 1:
       print('You survived! The ' + food_choice + ' were a good source of food and the ' + predator_choice + ' left you alone')

def main():
   print('SURVIVAL')
   print('')
   print('You are lost in a ' + biome_choice)
   print('You are living in a ' + shelter_choice)
   print('Your main food source is ' + food_choice)
   print('The main predator in the surrounding area are ' + predator_choice)
   print(how_long_choice + ' later')
   live()
   print('')
   print('If you like the code give it a thumbs up!')
   print('')
   print('For a different survival, press the run button again!')
   print('')
main()

suits =  ["clubs","spades","hearts","diamonds"]
ranks = ["As","2","3","4","5","6","7" ,"8","9","10", "jack","queen" ,"king"]
deck = [(i,j) for i in  suits for j in ranks]
crazy = "8"

# abstract display
def printCard(card):
    if unicd == "n":
        return card
    indices = [str(i) for i in range(1,10)] + ["A","B","C","D","E"]
    num = ""
    if card[0] == suits[0]:
        num = "&#x1F0C"
    if card[0] == suits[1]:
        num = "&#x1F0B"
    if card[0] == suits[2]:
        num = "&#x1F0A"
    if card[0] == suits[3]:
        num = "&#x1F0D"

    num = num + indices[ranks.index(card[1])]
    return nums

y = int(input('enter a number between 1 and 9:\n'))
for x in range(1,y):
    for k in range(2*y-x):
        print(' ',end='')
    for i in range (1,x):
        print(i,end='')
    for i in range(x,0,-1):
        print(i,end='')
    print('\n',end='')
for x in range(y,0,-1):
    for k in range(2*y-x):
        print(' ',end='')
    for i in range (1,x):
        print(i,end='')
    for i in range(x,0,-1):
        print(i,end='')
    print('\n',end='')


empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
    }
print(bierce)

lol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(lol))

print((lambda x, y, z: f'You: {x}\nCPU: {y}\n\n' + ('Draw!' if z[x]==z[y] else 'You won!' if z[x]==z[y]-1 or z[x]==z[y]+2 else 'You lost!'))(input("Давйте поиграем камень, ножница, бумага\nВведите\nrock/камень,\nscissors/ножницы,\npaper/бумага\nна Агл чтобы работал как надо: ").lower().strip(), __import__('random').choice(('rock', 'scissors', 'paper')), {'rock': 1, 'scissors': 2, 'paper': 3}))


def is_anagram(txt1, txt2):
    '''We've explained Counter in the previous trick'''
    return Counter(txt1) == Counter(txt2)

print(is_anagram('python', 'pothyn'))
print(is_anagram('anagram', 'nag a ram'))

for i in range(11):
    print(f'10 multiply by {i} = {10*i}')
else:
    print('Program ends')

with open('hello.py', 'w') as file:
    file.write('hello world')

try:
    a = open('hello.py', 'w')
    print('hello world', file=a)
except:
    pass
finally:
    a.close()

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
others = { 'Marx': 'Groucho', 'Howard': 'Moe'}
print(pythons.update(others))
print(pythons)

for i in range(53):
    for j in range(53,i,-1):
        print(j,end="")
    else:
        print()

a = [1,6,2,3]
a.sort()
print(a)

b = [7,1,6,5,5,2,3]
b.sort(reverse=True)
print(b)

c = ["Python", "Ruby", "c++", "Swift"]
c.sort(key=len)
print(c)

c.sort()
print(c)

d = [0,1,2,3,-2]
d.sort(key=lambda x:x**2-2*x,reverse=True)
print(d)


times = input("Введите количество раз, которые вы хотите певернуть монету: ");
print("");
heads = 0;
tails = 0;

for x in range(int(times)):
    rand = random.randint(0,1);
    if(rand == 0):
        print("heads");
        heads+=1;
    else:
        print("tails");
        tails+=1;
print("");
print("Result: " + str(heads) + " heads and " + str(tails) + " tails.");
print("Heads: " + str(round(((heads/int(times))*100),2)) + "%. Tails: " + str(round(((tails/int(times))*100),2)) + "%.");


builtins_content = dir(builtins)

for i, items in enumerate(builtins_content):
    if 'Error' in items:
        print(i, items)

print('Coin flip')

x = (int(random.randint(0, 1)))

if x == 0:
    print(x)
    print('Head')
else:
    print(x)
    print('Tail')

d=[int(x) for x in input("enter ur date of birth:\n").split()]
a=[int(x) for x in input("\nenter present day:\n").split()]
print("your life on earth is :")
print("days months years ")
if(a[0]<d[0] and a[1]<d[1]):
 print(30-(d[0]-a[0]),12-(d[1]-a[1])-1,a[2]-d[2]-1)
elif(a[1]<d[1]):
 print(a[0]-d[0],12-(d[1]-a[1]),a[2]-d[2]-1)
elif(a[0]<d[0]):
 print(30-(d[0]-a[0]),a[1]-d[1]-1,a[2]-d[2])
else:
 print(a[0]-d[0],a[1]-d[1],a[2]-d[2])
print("****************************")
print("please give me a like if u like my code ")

list=[23, 67, 11, 45, 66, 89, 48]
print("Second smallest element of",list,"=",end=" ")
list.remove(min(list))
scnd_smlst=min(list)
print(scnd_smlst)

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds[1][0])

words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)

friends = ['Harru', 'Harmione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)

numbers = [2, 1, 4.0, 3]
print(numbers.sort(reverse=True))
print(numbers)

a = [1, 2, 3]
print(a)
b = a
print(b)
a[2] = '#ТыЖеПрограммист'
print(a)
b = a
print(b)
b[1] = 'Но как же так'
print(b)
print(a)
b = a
b[0] = 'iшооооо!?'
print(b)

empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(tuple(marx_tuple))

print("Лень сегодня из-за плохого самочувствия")
print("Игра с рисования фигур")
print("#1-ромбовидная форма")
print("#2-Cross Shape:)")
print(" \n ")
print("Не забудьте высказать свое мнение по моему коду")
print(" \n ")
print("     *     ")
print("    ***    ")
print("   *****  ")
print("  *******  ")
print("  *******  ")
print("   *****  ")
print("    ***    ")
print("     *     ")
print(" \n ")
print("      @@@      ")
print("      @@@      ")
print("      @@@      ")
print("  @@@@@@@@$$$   ")
print("  @@@@@@@$$$$   ")
print("  @@@@@@$$$$$   ")
print("      @$$      ")
print("      $$$      ")
print("      $$$      ")

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)


user = int(input("Введите любое значение от 1 до 5: \n"))

jackopot = random.randint(1, 5)

if user == jackopot:
    print("Поздравляю, вы победили в игре")

else:
    print("Удачи в следующий раз!")

print ('Your random password')
a = ['1','2','3','4','5','6']
b = ['y','T','A','g','G']
c = ['t','Y','e','C']
d = ['A','a','B','b','C','c']
e = ['0','_','(',')','U']
f = ['4','&','j','K','x','_']
g = ['v','Q','H']
kk = ['7','8','9','0','666']
v = [[a],[b]]
k = [[c],[d]]
z = [[f],[g]]
kkk = [[e],[kk]]
j = random.choice(random.choice(v))
p = random.choice(random.choice(k))
kkkk = random.choice(random.choice(kkk))
y = random.choice(random.choice(z))
print(random.choice(p)+random.choice(j)+random.choice(a)+random.choice(j)+random.choice(kkkk)+random.choice(p)+random.choice(j)+random.choice(kkkk)+random.choice(p)+random.choice(kkkk))

empty_dict = {}
print(empty_dict)

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

los = [ 'ab', 'cd', 'ef' ]
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michal': 'Plian',
    'Terry': 'Jones',
    }
print(some_pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypous'}
first.update(second)
print(first)

pythons.clear()
print(pythons)
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael'}
print(pythons['Chapman'])

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())

empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
ood_numbers = {1, 3, 5, 7, 9}
print(ood_numbers)

set('letters')
print(set)

set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(set)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka' 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhttan': {'rye', 'vermouth', 'bitters'},
    'screwderiver': {'orenge juice', 'vodka'}
    }
for name, contents in drinks.items():
     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
          print(name)
bruss = drinks['black russian']
wruss = drinks['white russian']
print(bruss & wruss)
print(bruss | wruss)
print(bruss - wruss)
print(wruss - bruss)
print(bruss ^ wruss)
print(bruss <= wruss)
print(wruss >= bruss)
print(wruss > bruss)

def my_func():

    print("* * * *")
    print("*     *")
    print("*     *")
    print("* * * *")

my_func()
my_func()

def bb():

    print(" * ")
    print("* *")
    print("* *")
    print(" * ")

bb()


print('OS:', os.name)
print('System:', platform.system())
print('Architecture:', platform.architecture)
print('Version:', platform.version())
print('Release:', platform.release())
print('CPU Count:', os.cpu_count())
print('PATH:', os.path)
print()
print('-'*20 + '1 odject detected by the RadaR[::-1]')

input("Нажмите ENTER: ")

[globals().__setitem__('robot',lambda *a:[sum(a[1::4]) - sum(a[3::4]),sum(a[::4]) - sum(a[2::4])]), [print(*i, '==>',robot(*i)) for i in [[20,30,40,50], [10,20,30,40],[20,30,10,40],[0,0],[50,40,8,2,5]] ]]

def primeGenerator():
    n=2
    composites={}
    while True:
        if n not in composites:
            yield n
            composites[n*n]=[n]
        else:
            for p in composites[n]:
                if p+n in composites:
                    composites[p+n].append(p)
                else:
                    composites[p+n]=[p]
            del composites[n]
        n=n+1

pg=primeGenerator()

print([next(pg) for _ in range(50)])

print(os.environ)
print(os.listdir('C://Users/default'))

class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type

class Pet(Animal):
    def __init__(self,petname,owner):
        Animal.__init__(self,"dog","mammal")
        self.petname=petname
        self.owner=owner
pet=Pet("Doddums","Debbie")

print(pet.owner,"has a",pet.name,"called",pet.petname)


"""Введите два слова, чтобы проверить, являются ли анаграммы"""

word1 = input("Введите слова: ")
word2 = input("Введите слова еще раз: ")

def is_anagram(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    return Counter(word1.replace(' ','')) == Counter(word2.replace(' ',''))

print(f"The given words: '{word1}' & '{word2}'\nare anagerams) -> {is_anagram(word1, word2)}")

print(2 * 1_000)
print(1_234_567 + 1_234.567)
print(3_3)
print(float("1_234.567"))
print(123.456_789)

class Animal:
    def __init__(self, name, category, limbs):
        self.name=name
        self.category=category
        self.limbs=limbs

animal=Animal("dog","mamml",4)
print("A",animal.name,"is a",animal.category,".")
print("It has",animal.limbs,"limbs.")

num = input("")
total = 0
for i in num:
    total +=int(i)
print(total)

def recurse(n):
    if n>10:
        print(n, end="")
    else:
        return recurse(n+1)

print(1)
recurse(1)
print("+")

def double_str(string):
    for x in string:
        print(x * 2)
double_str("ABCD")

def StateMchine(word):
    word = str(word)
    state = 0
    for c in word:
        try: c = int(c)
        except: return 'wrong character'
        pos = 1<<(c+1)
        state = ((state|pos)>>1<<1)+bool(pos&state)
    return state&1

cases = ['11111','000','101101','123456789','20351','202']
for case in cases:
    print(case,StateMchine(case))

"""
[вызов Антона Белера]
Создайте конечный автомат, который может узнать, является ли данное слово, состоящее из «0» и «1», частью этого языка:
Длина слова больше 1
Слово заканчивается на символе, который уже видел ранее в слове

Это конечный автомат, а не питон один лайнер
(Но если вы сделали конечный автомат, не стесняйтесь сделать также и oneliner)

[Вызов +]
Создайте конечный автомат, который находит те же слова, но теперь слово может состоять из «0», «1» и «2».

Счастливого мышления!
(Для решения либо вы можете написать мне)

[Вызов ++]
Сколько нужно состояний, если меняется алфавит слова. (Понятия не имею, насколько это возможно)
"""

"""
  @ Автор: Хуан Баньос 🇪🇸
 
  * Функция лямбда-пара-эль-cuadrado de los 10 простых номеров.
 
* Лямбда-функция для квадрата первых 10 натуральных чисел.
  
  ┏━┓╋┏┓┏┓ ТМ
  ┃╋┣┳┫┗┫┗┳━┳━┳┓
  ┃┏┫┃┃┏┫┃┃╋┃┃┃┃
  ┗┛┣┓┣━┻┻┻━┻┻━┛
  ╋╋┗━┛
"""

list_nums = [0,1,2,3,4,5,6,7,8,9]
squared_nums = [x**2 for x in list_nums]
print("List with the first 10 natural numbers")
print(list_nums)
print()
print("List with list_nums squares")
print(squared_nums)

a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))
print(a.union(b))
print(a - b)
print(a.difference(b))
print(a ^ b)
print(a.symmetric_difference(b))
print(a <= b)
print(a.issubset(b))
print(a <= a)
print(a.issubset(a))
print(a < b)
print(a < a)
print(a >= b)
print(a.issuperset(b))
print(a >= a)
print(a.issuperset(a))
print(a > b)
print(a > b)

a = [[1+sum(range(n))+i for i in range(n)] for n in range(1, int(input("Введите идиницу: "))+1)]

print("Floyd's Triangle:")
for r in a:
    print(*r)

print("\nReverse Floyd's Tringle:")
for r in a[::-1]:
    print(*r[::-1])

Dna = str.maketrans(
    'ATGC',
    'TACG'
)

inp = (input("Введите Слова ATGC или TACG: ") or 'catage').upper()

print((str.translate(inp, Dna)))

n = int(input("Введите число 2 или 3: "))
k = n // 3
if (k % 2 == 0): print(n - k)
else: print(n - k)

print("===============")

if ((i := (j := int(input("И СНОВА Введите число 2 или 3: "))) // 3) % 2 == 0): print(i + j)
else: print(j - i)

def in_r4wa():

    print("############")
    print("#  ######  #")
    print("#  ######  #")
    print("############")
    print("#          #")
    print("############")

in_r4wa()

def algo(x,y, z=True):
    if x<y:
        return algo(y,x,z)
    print()
    while y!=0:
        if z:
            print(f'{__import__("math").floor(x/y)}, {y}, {x%y}')
            x,y = y,x%y
    if z:
        print(f'Greatest common divisor is => {x}')
        return x

algo(42,58)

"""Привет и время использования Python
Код кредита: A.Sarevant (идея и рубиновая версия)
код: Micheal BlackRose
Примечения: этот код-часовой пояс"""

import time as t

gm_greet1 = '''Доброе утро
Раннее утро, вы либо пишете код, либо собиратесь спать или бодроствовать'''

gm_greet2 = '''Доброе утро
Надеюсь, вы сьлеи перерыв на завтрак, хорошего вам дня'''
greet3 = '''Добрый день
Надеюсь у тебя хороший день.'''
greet4 = '''Спокойной ночи
Вы либо собираетесь кодировать или спать.
Хорошей ночи'''

def get_time():
    time_sec =t.gmtime()
    hour = time_sec.tm_hour
    mins = time_sec.tm_min
    sec = time_sec.tm_sec
    return (hour, mins, sec)

def timelen(xy):
    if (xy < 10):
        xy = "0" + str(xy)
    return xy

def greetings():
    curr_time = get_time()
    h, m, s = curr_time

    m = timelen(m)
    s = timelen(s)
    h = int(h)

    if (h + 1 == 24):
        h = 0
    else:
        h = h + 1

    the_time = f"The current time is {h}:{m}:{s} (h/mm/ss) \n"

    if (h >= 0 and h <= 6):
        print(the_time)
        return gm_greet1
    elif (h >= 7 and h < 12):
        print(the_time)
        return gm_greet2
    elif (h >= 12 and h <= 16):
        print(the_time)
        return greet3
    else:
        print(the_time)
        return greet4

print(greetings())

marx_list = ['Groucho', 'Cihco', 'Harpo']
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
print(marx_list[2])
print(marx_dict['Groucho'])

stooge = ['Moe', 'Curly', 'Larry']
tuple_of_lists = [marxes, pythons, stooge]
tuple_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooge}
print(tuple_of_lists)

print("""Some new features of Python 3.8:\n\n
1. Walrus Operator (Assign and Compare at the same time):

[Code] >>>
mydict = {"name": "Python", "age": 10}

# Prior to 3.8
name = mydict.get("name")
if name:
    print(f"Name is {name}")

height = mydict.get("height")
if height:
    print(f"Height is {height}")

# In 3.8
if name := mydict.get("name"):
    print(f"Name is {name}")

if height := mydict.get("height"):
    print(f"Height is {height}")

[Output] >>>""")
# ---------- [1. Настоящий код здесь] ------------
mydict = {"name": "Python", "age": 10}

# До 3.8
name = mydict.get("name")
if name:
    print(f"Name is {name}")

height = mydict.get("height")
if height:
    print(f"Height is {height}")

# В 3.8
if name := mydict.get("name"):
    print(f"Name is {name}")

if height := mydict.get("height"):
    print(f"Height is {height}")
# --------------------------------------------

print("""\n
2. Print Variable Name and Value at the same time:\n

[Code] >>>
country = "India"
capital = "New Delhi"

print(f"{country=}\\n{capital=}")

[Output] >>> """)

# ---------- [2. Настоящий код здесь] ------------
country = "India"
capital = "New Delhi"

print(f"{country=}\n{capital=}")
# -------------------------------------------

print("""\n
3. Positional only arguments:\n

[Code] >>>
# Without positional only parameters
def add(a, b):
    return a + b

print(f"Sum is {add(b=2, a=1)}")

# With positional only parameters
def add(a, b, /):
    return a + b

print(f"Sum is {add(1, 2)}")  # No Error
print(f"Sum is {add(b=2, a=1)}") # Results in Error

[Output] >>>""")

# ---------- [3. Настоящий код здесь] ------------
# Без позиционных параметров
def add(a, b):
    return a + b

print(f"Sum is {add(b=2, a=1)}")

# -------------------------------------------

print("---------------------------------------\n")
num = input("Введите число: ");
a= int(num[0]+num[-1]);
if len(num) > 2:
    print ((num + " is a gapful number") if int(num)% int(a)== 0 else (num  + " is not a gapful number"))
else:
    print ("According to Conditions :\nNumber should be 3 digits or longer\n")

print("\n---------------------------------------\n")
print("This is first try with python...\nHope you like it...")
print("\n---------------------------------------\n")

from random import sample
a = []
b = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYxzZ@#$%&-+.?!*0123456789"

a.append(sample(b,8))

a2 = str(a)

print(a2.replace(", ", "").replace("'", "").replace("]", "").replace("[", ""))

matrix = """X.XX.XXXX...X...XX..
XX.X.XX...XX.XXX.XXX
XX...X.X...XXX.XX...
X.X....X.X..X.XXX...
...X....X.......X.XX
"""

matrix = matrix.split("\n")
matrix.pop(-1)
matrix.pop(0)

def patDownPossible(matrix, x, y):
    if y < len(matrix)-1:
        if matrix[y][x] == "X":
            return False
        if matrix[y+1][x] == "X":
            if x-1 >= 0 and matrix[y][x-1] != "X":
                if patDownPossible(matrix, x-1, y-1):
                    return  True
            if x+1 < len(matrix[0]) and matrix[y][x+1] != "X":
                if patDownPossible(matrix, x-1, y-1):
                    return True
            return False
        else:
            return patDownPossible(matrix, x, y+1)
    else:
        return True

for row in matrix:
    print(row)
for i in range(len(matrix[0])):
    print(int(patDownPossible(matrix, i, 0)), end="\n")

alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmnop'
alphabet += 'qrstuv'
alphabet += 'wxyz'
print(alphabet)

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
small = True
if furry:
    if small:
        print("It's cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee puple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

count = 1
while count <= 5:
    print(count)
    count += 1

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':   #Выход
        break
    number = int(value)
    if number % 2 == 0:  # Нечетное число
        continue
    print(number, "squared is", number*number)

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:   # перерыв не называется
    print('No even number found')

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
for rabbits in rabbits:
    print(rabbits)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col, Mustard'}
for card in accusation:    # или for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, countents in accusation.items():
    print('Card', card, 'has the contents', countents)

cheeses = []
for cheeses in cheeses:
    print('This shop has some lovely', cheeses)
    break
else:   # отсуствие перывания означает, что сыр нет
    print('This is not much of a cheese shop, is it')

cheeses = []
found_one = False
for cheeses in cheeses:
    found_one = True
    print('This shop has some lovely', cheeses)
    break
if not found_one:
    print('This is not much of a cheese shop, is it')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruits, drinks, desserts in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drinks, "eat", fruits, "enjoy", desserts)

for x in range(0,3):
    print(x)

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1,6):
    number_list.append(number)
print(number_list)

number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)

a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

word = 'letters'
letters_counts = {letter: word.count(letter) for letter in word}
print(letters_counts)

word = 'letters'
letters_counts = {letter: word.count(letter) for letter in set(word)}
print(letters_counts)

a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

number_thing = (number for number in range(1, 6))
for number in number_thing:
    print(number)

import sys,subprocess
def install(package):
    subprocess.call([sys.executable, "-m", "pip","-q","install", package])

install('geocoder')

def do_nothing():
    pass
print(do_nothing())

def make_a_sound():
    print('quack')
print(make_a_sound())

def agree():
    return True
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')
print(agree())

def echo(anything):
    return anything + ' ' + anything
echo('Rumplestiltskin')

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is. but only bees can see it."
    else:
        return "I've never heard of the color" + color + "."
comment = commentary('blue')
print(comment)

thige = None
if thige:
    print("It's some thing")
else:
    print("It's no thing")

def is_none(thing):
    if thing is None:
        print("It's Nome")
    elif thing:
        print("It's True")
    else:
        print("It's False")
print(is_none(None))
print(is_none(True))
print(is_none(False))
print(is_none(0))
print(is_none(0.0))
print(is_none(()))
print(is_none([]))
print(is_none({}))
print(is_none(set()))

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree':  entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))

count = 1
while count <= 100:
    print(count)
    count += 1

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'dughnut'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

print(buggy('a'))
print(buggy('b'))

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

print(nonbuggy('a'))
print(nonbuggy('b'))

def print_args(*args):
    print('Positional argument tuple:', args)

print(print_args())
print(print_args(3, 2, 1, 'Wait!', 'uh...'))

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print(print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax'))

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print(print_kwargs(wine='merlot', entree='mutton', dessert='macaroon'))

def echo(anything):
    'echo retuarns its input argument'
    return anything

def print_if_true(thing, check):
    if check:
        print(thing)

help(echo)

print(echo.__doc__)

def answer():
    print(42)

print(answer())

def run_something(func):
    func()

print(run_something(answer))
print(type(run_something))

def add_args(arg1, arg2):
    print(arg1 + arg2)

print(type(add_args))

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

print(run_something_with_args(add_args, 5, 9))

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

def knighits(saying):
    def inner(quote):
        return "We are the khights who say: '%s'"% quote
    return inner(saying)

print(knighits('Ni!'))

def knighits2(saying):
    def inner2():
        return "We are the knignhts who say: '%s'" % saying
    return inner2

a = knighits2('Duck')
b = knighits2('Hasenpefeffer')

print(type(a))
print(type(b))
print(a)
print(b)
print(a())
print(b())

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

print(edit_story(stairs, lambda word: word.capitalize() + '!'))

print(sum(range(1, 101)))

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)

ranger = my_range(1, 5)
print(ranger)

for x in ranger:
    print(x)

def ocu(a, b):
    def flex(c, d):
        return c + d
    return flex(a, b)

print(ocu(94, 45,))

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func,__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(5, 3))

cooler_add_ints = document_it(add_ints) # мануальное присваивание декоратора
print(cooler_add_ints(3, 5))

@document_it
def add_ints(a, b):
    return a + b

print(add_ints(10, 10))

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(78, 45))

@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(1, 1))

animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print(print_global())

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

print(change_local())
print(animal)
print(id(animal))

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

print(animal)
print(change_and_print_global())
print(animal)

animal = 'fruitbat'
def change_local():
    animal = 'wombat' # локальная переменная
    print('locals:', locals())

print(animal)
print(change_local())
print('globals', globals()) # немного переформатировано для представления
print(animal)

def amzing():
    '''Это amazing функторион
    Хотите увидеть это снова?'''
    print('Эта функция называется:', amzing,__name__)
    print('И его доктрина:', amzing,__doc__)

print(amzing())

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got', position)

short_list = [1, 2, 3]
while True:
    value = input('Position[q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

kok = '''
Хотел бы я знать, зачем звезды светятся...
Наверно, зачем, чтобы рано или поздно
каждый мог вновь отыскать свою.
Автор стих: Антуан де Сент-Экзюпери
Книге: Маленький Принц'''

print(kok)

print("\N{winking face}")
print("\N{grinning face}")
print("\N{angry face}")
print("\N{battery}")

print(sum(range(1, 101)))
print(sum(range(9, 909)))
print(sum(range(2, 202)))

import sys
print('Program argumnts:', sys.argv)

import random
def get_description():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)

print(get_description())

import sys
for place in sys.path:
    print(place)

periodic_table = {"Hydrogen": 1, 'Helim': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

from collections import defaultdict
def no_idea():
    return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1
for food, count in food_counter.items():
    print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1
for food, count in dict_counter.items():
    print(food, count)

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)
print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('halibut'))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))

import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

import itertools
def multiply(a, b):
    return a * b
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])
print(pprint(quotes))

class Person():
    def __init__(self, name):
        self.name = name
hunter = Person('АХАХАХА')

print('АЗАЗА:', hunter.name)

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_posh(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())
print(give_me_a_yugo.need_a_posh())

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esguire"

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(person.name)
print(doctor.name)
print(lawyer.name)
print(bob.name)
print(bob.email)

car = Car()
print(car.exclaim())

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.name = 'Daffy'
fowl.set_name('Daffy')
print(fowl.name)
print(fowl.get_name())

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
fowl.name = 'Donald'
print(fowl.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
c.radius = 7
print(c.radius)
print(c.diameter)

class Yura():
    def __init__(self, name):
        self.name = "Кто он " + name

yura = Yura('Программист!?')
print(yura.name)

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objest.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
print(A.kids())

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

print(CoyoteWeapon.commercial())

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunter1 = QuestionQuote('Bugs Bunny', "What's up. doc")
hunter2 = ExclamationQuote('Daffy Duck', "It's rabbit season")

print(hunter.who(), 'says:', hunter.says())
print(hunter1.who(), 'says:', hunter1.says())
print(hunter2.who(), 'says:', hunter2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says:', obj.says())

print(who_says(hunter))
print(who_says(hunter1))
print(who_says(hunter2))
print(who_says(brook))

class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))
print(first == second)
print(first == third)

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
frist = Word('HA')
frist = Word('he')

print(first == second)
print(first == third)
print(first)

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')

tail = Tail('Long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
print(duck.about())

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck)
print(duck.bill)
print(duck.tail)
print(duck.bill, duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)

print(duck2)

duck3 = duck2._replace(tail = 'magnificent', bill = 'long')

print(duck3)

duck_dict = {'bill': 'wige orange', 'tail': 'long'}

duck_dict['color'] = 'green'

print(duck_dict)

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", name="%s"' % (value, name, value2))

print(unicode_test('A'))
print(unicode_test('$'))
print(unicode_test('\u00a2'))
print(unicode_test('\u20ac'))
print(unicode_test('\u2603'))
print(unicode_test('\u00e9'))
print(unicode_test('Y'))
print(unicode_test('U'))
print(unicode_test('R'))
print(unicode_test('A'))
print(unicode_test('\u272A'))
print(unicode_test('\u0040'))


place = 'cafe'
print(place)
place = 'caf\u00e9'
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)
print(type(place))

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)
drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

print(len('$'))
print(len('\U0001f47b'))
print(len('#'))

snowman = '\u2603'
print(len(snowman))

ds = snowman.encode('utf-8')
print(len(ds))
print(ds)

print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

place3 = place_bytes.decode('latin-1')
print(place3)

place4 = place_bytes.decode('windows-1252')
print(place4)

print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)
print('%d%%' % 100)
print('%f%%' % 9.999)

actor = 'Richard Gere'
cat = 'Chester'
weignt = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weignt))

n = 42
f = 7.03
s = 'string cheese'

print('%d %f %s' % (n, f, s))
print('%10d %10f %10s' % (n, f, s))
print('%-10d %-10f %-10s' % (n, f, s))
print('%10.4d %10.4f %10.4s' % (n, f, s))
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))

print('{0:!^20s}', format('BIG SALE'))

import re
source = 'Young Frankenstein'
m = re.match('You', source) # 1 функция начинает работать с начала источника 2 якор, в начале строки делает то же самое
if m: # функция возрашает обьект: делайте это, чтобы увидеть, что что совпало
    print(m.group())
m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m: # match returns an object
    print(m.group())

m = re.search('Frank', source)
if m: # функция search возращает обьект
    print(m.group())

m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.', source)
print(m)

m = re.findall('n.?', source)
print(m)

m = re.split('n', source)
print(m) # функция split возращает список

m = re.sub('n', '?', source)
print(m) #  функция sub возращает строку

import string
printable = string.printable

print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'

print(re.findall('\w', x))

source = '''I wish I may, I wish I minght... Have a dish of fish tonight'''

print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish$', source))
print(re.findall('fish tonight\.$', source))
print(re.findall('[wf]ish', source))
print(re.findall('[wsh]+', source))
print(re.findall('ght\W', source))
print(re.findall('I (?=wish)', source))
print(re.findall('(?<=I) wish', source))
print(re.findall('\bfish', source))
print(re.findall(r'\bfish', source))

m = re.search(r'(. dish\b).*(\bfish)', source)

print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)

print(m.group())
print(m.groups())
print(m.group("DISH"))
print(m.group('FISH'))

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_byte_array = bytearray(blist)

print(the_bytes)
print(the_byte_array)

print(b'\x61')

the_byte_array = bytearray(blist)
the_byte_array[1] = 27

print(the_byte_array)

the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))

print(the_bytes)

poem = '''Там была молодая леди по имени Брайт
Чья скорость была намного быстрее света:
Она начала один день
Относительно.
И вернулся прошлой ночью'''
fout = open('relativity', 'wt')

print(len(poem))
print(fout.write(poem))
print(poem, file=fout)
print(poem, file=fout, sep='', end='')
print(fout.close())

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')

print(fout.close())

fin = open('relativity', 'rt')
poem = fin.read()

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

print(fin.close())
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

print(fin.close())
print(len(poem))

fin = open('relativity', 'rt')
lines = fin.readline()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')

local_barmy = ['\nYura', 'Dania', 'Cyril', 'Zhora']
nura = '  '
joined = nura.join(local_barmy)
print(joined)

years_list = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
print(years_list[3])
print(years_list[6])

import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
 ['Ernst', 'Blofeld'],
    ]
with open('villains', 'wt') as fout: # менеджер контекста
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)

import datetime
now = datetime.datetime.utcnow()
now_str = str(now)
print(now)

import pickle
import datetime
nowl = datetime.datetime.utcnow()
pickled = pickle.dumps(nowl)
now2 = pickle.loads(pickled)

print(nowl)
print(now2)

import pickle
class Tiny():
    def __str__(self):
        return 'tiny'
obj1 = Tiny()
pickled = pickle.dumps(obj1)
obj2 = pickle.loads(pickled)

print(obj1)
print(str(obj1))
print(pickled)
print(obj2)
print(obj2)

import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
    sa.Column('critter', sa.String, primary_key=True),
    sa.Column('count', sa.Integer),
    sa.Column('damages', sa.Float)
    )
meta.create_all(conn)
result = conn.execute(zoo.select())
rows = result.fetchall()

print(conn.execute(zoo.insert(('bear', 2, 1000.0))))
print(conn.execute(zoo.insert(('weasel', 1, 2000.0))))
print(conn.execute(zoo.insert(('duck', 10.0))))
print(rows)

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)
Base.metadata.create_all(conn)
frist = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)

print(first)

import dbm
db = dbm.open('definitions', 'c')
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

print(len(db))
print(db['pesto'])
print(db['ketchup'])
print(db['mustard'])

print(db.close)
db = dbm.open('definitions', 'r')
print(db['mustard'])

import time
now = time.time()

print(now)

import os

print(os.listdir('.'))
print(os.getpid())
print(os.getcwd())

import glob

print(glob.glob('m*'))
print(glob.glob('??'))
print(glob.glob('m??????e'))
print(glob.glob('[klm]*e'))

import subprocess
ret = subprocess.getoutput('date')

print(ret)

import calendar

print(calendar.isleap(1900))
print(calendar.isleap(2020))

from datetime import date
halloween = date(2004, 8, 28)
datetime.date(2004, 8, 28)

print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())

from datetime import date
now = date.today()

print(now)

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
yesterday = now - one_day

print(tomorrow)
print(now + 17*one_day)
print(yesterday)

from datetime import time
noon = time(12, 0, 0)

print(noon)
print(noon.hour)
print(noon.minute)
print(noon.microsecond)

from datetime import datetime
now = datetime.now()

print(now)
print(now.day)
print(now.hour)
print(now.minute)
print(now.microsecond)

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)

print(noon_today)
print(noon_today.date())
print(noon_today.time())

import time
now = time.time()
tm = time.localtime(now)

print(now)
print(time.ctime(now))
print(time.localtime(now))
print(time.gmtime(now))
print(time.mktime(tm))

import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()

print(t)
print(time.strftime(fmt, t))

from datetime import date
some_day = date(2020, 8, 28)
fmt = "It's %B %d, %Y, local time %I:%M:%S%p"

print(some_day.strftime(fmt))

from datetime import time
some_time = time(10, 35)

print(some_day.strftime(fmt))

def ftoc(f_temp):
    "Convert Fahreheit temperature <f_temp> to Celsius and return it."
    f_boil_temp = 212.0
    f_freeze_temp = 32.0
    c_boil_temp = 100.0
    c_freeze_temp = 0.0
    f_range = f_boil_temp - f_freeze_temp
    c_range = c_boil_temp - c_freeze_temp
    f_c_ratio = c_range / f_range
    c_temp = (f_temp - f_freeze_temp) * f_c_ratio + c_freeze_temp
    return c_temp
if __name__ == '__main__':
    for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print('%f F => %f C' % (f_temp, c_temp))

import logging
logging.debug("Looks like rain")
logging.info("And hail")
logging.warn("ЧТО НОВОГО А?")
logging.error("Was that lightning?")
logging.critical("Finally new text.py file updates Yes Yes Dadad UUUAAAAAAAA!")

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("It's raining again")
logging.info("With hall the size of hailstones")

import logging
logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warn("I need my axe")

import logging
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")

from time import time
t1 = time()
num = 5
num *= 2

print(time() -t1)

from time import time, sleep
t1 = time()
sleep(1.0)

print(time() -t1)

from timeit import timeit
def make_list_1():
    result = []
    for value in range(1000):
        result.append(value)
    return result
def make_list_2():
    result = [value for value in range(1000)]
    return result
print('make_list_1 takes', timeit(make_list_1, number=1000), 'seconds')
print('make_list_2 takes', timeit(make_list_2, number=1000), 'seconds')

import math

print(math.pi)
print(math.e)
print(math.fabs(98.6))
print(math.fabs(-271.1))
print(math.floor(543.2))
print(math.floor(-45.6))
print(math.ceil(666.0))
print(math.ceil(-235.012))
print(math.factorial(0))
print(math.factorial(1))
print(math.factorial(5))
print(math.factorial(7))
print(math.factorial(100))
print(math.log(10.0))
print(math.log(math.e))
print(math.log(9, 9))
print(math.pow(4, 5))
print(2**8)
print(4.0**6)
print(math.sqrt(100.0))

x = 3.0
y = 2.0

print(math.hypot(x, y))

print(math.sqrt(x*x + y*y))
print(math.sqrt(x**4 + y**45))
print(math.radians(360.0))
print(math.degrees(math.pi))

print(5)
print(9j)
print(3 + 4j)
print(1j * 1j)
print((5 + 4j) * 1j)

x = 10.0 / 3.0
print(x)

from decimal import Decimal
price = Decimal('29.99')
tax = Decimal('0.7')
total = price + (price * tax)
print(total)

from fractions import Fraction
Fraction(1, 3) * Fraction(2, 3)
Fraction(4.0/5.0)

import numpy as np
s = np.array([2, 4, 6, 8])
b = np.arange(10)
v = np.arange(8, 110)
j = np.arange(2.0, 8.9, 8.3)
g = np.arange(10, 2, -1.9, dtype=np.float)
a = np.zeros((8,))
o = np.zeros((2, 4))
k = np.ones((3, 9))
m = np.random.random((5, 100))
n = np.arange(10)
n = n.reshape(5, 2)
l = [ [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
p = np.arange(10)
p = p.reshape(2, 5)
p[:, 2:4] = 1000
coefficients = np.array([ [4, 5], [1, 2] ])
dependents = np.array([20, 13])
answers = np.linalg.solve(coefficients, dependents)
product = np.dot(coefficients, answers)

print(s)
print(s.ndim)
print(s.size)
print(s.shape)
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(v)
print(j)
print(g)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(o)
print(o.ndim)
print(o.shape)
print(o.size)
print(k)
print(m)
print(n)
print(n.ndim)
print(n.shape)
print(n.size)
print(n)
print(l[1][2])
print(p)
print(p[0, 2:])
print(p[-1, :3])
print(answers)
print(4 * answers[0] + 5 * answers[1])
print(1 * answers[0] + 2 * answers[1])
print(product)
print(np.allclose(product, dependents))

from numpy import *
a = arange(5)
a *= 3
b = zeros((2, 5)) + 17.0
g = arange(10)
j = zeros((3,1)) + g

print(a)
print(b)
print(j)

print("Начертим треугольник на 35, 40 см")

fa = 35
fb = 35
fc = 40

s = fa + fb + fc
p = fa * fb * fc

print("Результат решения треугольника s:", s, "p:", p)

age = 15
name = 'Aizec'

print('Возраст {} -- {} лет.'.format(name, age))
print('Почему {} забавляется с этим Python!?'.format(name))

#десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))
# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))

i = 5;
print(i);
i = i + 1
print(i)

s = '''Это многострочная строка.
Это вторая её строчка.'''
print(s)

s = 'Это строка. \
Это строка продолжается'
print(s)

#Сложение. Суммирует два объекта
print(3 + 5, 'a' + 'b')
#Вычитание. Даёт разность двух чисел; если первый операнд отсутствует, он считается равным нулю
print(-5.2, 50 - 24)
#Умножение. Даёт произведение двух чисел или возвращает строку, повторённую заданное число раз.
print(8 * 4, 'la' * 12)
#Возведение в степень. Возвращает число х, возведённое в степень y
print(3 ** 4)
#Деление. Возвращает частное от деления x на y
print(4 / 3)
#Целочисленное деление. Возвращает неполное частное от деления
print(4 // 3, -4 // 3)
#Деление по модулю. Возвращает остаток от деления
print(8 % 3, -25.5 % 2.25)
#Сдвиг влево. Сдвигает биты числа влево на заданное количество позиций. (Любое число в памяти компьютера представлено в виде битов - или двоичных чисел, т.е. 0 и 1)
#Сдвиг вправо. Сдвигает биты числа вправо на заданное число позиций.
print(2 << 2, 11 >> 1)
#Побитовое И. Побитовая операция И над числами
print(5 & 3)
#Побитовое ИЛИ. Побитовая операция ИЛИ над числами
print(5 | 3)
#Побитовое ИСКЛЮЧИТЕЛЬНО ИЛИ. Побитовая операция ИСКЛЮЧИТЕЛЬНО ИЛИ
print(4 ^ 7)
#Побитовое НЕ. Побитовая операция НЕ для числа x соответствует -(x+1)
print(~5)
#Меньше. Определяет, верно ли, что x меньше y. Все операторы сравнения возвращают True или False. Обратите внимание на заглавные буквы в этих словах
#Больше. Определяет, верно ли, что x больше y
print(5 < 3, 3 < 5, 3 < 5 < 7, 5 > 3)
#Меньше или равно. Определяет, верно ли, что x меньше или равно y
#Больше или равно. Определяет, верно ли, что x больше или равно y
x = 4
y = 6
print(x <= y)
x = 4
y = 3
print(x >= y)
#Равно. Проверяет, одинаковы ли объекты
x = 2
y = 2
d = 'jon'
f = 'Jon'
t = 'jon'
r = 'jon'
print(x == y, d == f, t == r)
#Не равно Проверяет, верно ли, что объекты не равны
x = 2
y = 3
h = 2
t = 2
print(x != y, h != t)
#Логическое НЕ. Если x равно True, оператор вернёт False. Если же x равно False, получим True
g = True
k = False
print(not g, not k)
#Логическое И. x and y даёт False, если x равно False , в противном случае возвращает значение y
z = False
v = True
print(z and v)
#Логическое ИЛИ. Если x равно True, в результате получим True, в противном случае получим значение y
u = True
o = False
print(o or u)

length = 5
breadth = 2
area = length * breadth
print('Площадь равна', area)
print('Периметр равен', 2 * (length + breadth))

number = 25
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздравляю, вы угадали,')#Начало нового блока
    print('(хотя и не выиграли никакого приза!)')#Конец нового блока
elif guess < number:
    print('Нет, загадонное число немного больше этого.')#Ещё один блок
    #Внутри блока вы можете выполнять всё, что угодно...
else:
    print('Нет, загадонное число немного меньше этого.')
    #Чтобы попасть сюда, guess должно быть больше, чем number
print('Завершено')
#Это последнее выражение выполняется всегда после выполнения оператора if

number = 35
running = True

while running:
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False #Это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
    #Здесь можете выполнить всё что вам ещё нужно

print('Завершение.')

for i in range(1, 5):
    print(i)
else:
    print('Цикл for закончен')

while True:
    s = input('Введите что-нибудь: ')
    if s == 'end':
        break
    print('Длина строки: ', len(s))
print('Завершение')

while True:
    s = input('Введите что-нибудь: ')
    if s == 'end':
        break
    if len(s) < 5:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длиный')
    #Разные другие действия здесь...

def sayHello():
    print('*фраза*')#Блок, принадлежащий функции
#Конец функции

print(sayHello())# вызов функции
print(sayHello())# ещё один вызов функции

def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'ровно', b)
    else:
        print(b, 'максимально')

printMax(6, 7)# прямая передача значений

x = 8
y = 9

print(printMax(x, y))# передача переменных в качестве аргументов

x = 50

def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

print(func(x))
print('x по-прежнему', x)

x = 50

def func():
    global x

    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

print(func())
print('Значение x составляет', x)

def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5
    print(func_inner())
    print('Локальное x сменилось на', x)

print(func_outer())

def say(message, times = 1):
    print(message * times)

print(say('Беды с'))
print(say('Ба', 2))

def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)

print(func(3, 7))
print(func(25, c=24))
print(func(c=50, a=100))

def total(a=5, *numbers, **phonebook):
    print('a', a)
    #проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    #проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

#!/usr/bin/python

def maxinum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y

print(maxinum(2, 3))

def printMax(x, y):
    '''Выводит максимальное из двух чисел.
        Оба значения должны быть целыми числами.'''
    x = int(x)# конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

print(printMax(3, 5))
print(printMax.__doc__)

import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\nПеременная PYTHONPATH содержит', sys.path, '\n')

from math import *
n = int(input("Введите диапазон:- "))
p = [2, 3]
count = 2
a = 5
while (count < n):
    b=0
    for i in range(2,a):
        if (i <= sqrt(a)):
            if (a % i == 0):
                print(a,"непростое")
                b = 1
            else:
                pass
    if (b != 1):
        print(a,"простое")
        p = p + [a]
    count = count + 1
    a = a + 2
print(p)

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')

import mymodule

mymodule.sayhi()
print('Версия', mymodule.__version__)

import sys # получим список атрибутов модуля 'sys'
dir(sys)
dir() # получим список атрибутов текущего модуля
a = 5 # создадим новую переменную 'a'
dir()
del a # удалим имя 'a'
dir()

#Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупки.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Теперь мой список покупок:', shoplist)

zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))

new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1 + len(new_zoo[2]))

# 'ab' - сокращение от 'a'ddress'b'ook

ab = {'Swaroop':'swaroop@swaroopch.com',
      'Larry':'larry@wall.org',
      'Matsumoto':'matz@ruby-lang.org',
      'Spammer':'spammer@hotmail.com',
      'Yura':'yura.mukhin@gmail.com'
    }

print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Swaroop']

print('\nВ адресной книге {0} контакт\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

name = 'swaroop'

# Операция индексирования
print('Элемент 0', shoplist[0],'\nЭлемент 1', shoplist[1], '\nЭлемент 3', shoplist[3], '\nЭлемент -1', shoplist[-1], '\nЭлемент -2', shoplist[-2])
print('Символ 0:', name)

# Вырезка из списка
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])
# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

print(shoplist[::1], '\n', shoplist[::2], '\n', shoplist[::3], '\n', shoplist[::-1])

bri = set(['Бразилия', 'Россия', 'Индия'])

print('Индия' in bri)
print('США' in bri)
bric = bri.copy()
bric.add('Китай')
bric.issuperset(bri)
bri.remove('Россия')
print(bri & bric)#Or bri.intersection(bric)

print('Простое присваивание')
mylist = shoplist# mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0]# Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один
# объект.

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]# создаём копию путём полной вырезки
del mylist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные

name = 'Mukhin'# Это объект строки

if name.startswith('Muk'):
    print('Да, строка начинается на "Muk"')

if 'h' in name:
    print('Да, она содержит строку "h"')

if name.find('in') != -1:
    print('Да, она содержит строку "in"')

delimiter = '_*_'

mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

poem ='''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

f = open('poem.txt', 'w')# открываем для записи (writing)
f.write(poem)# записываем текст в файл
f.close()# закрываем файл

f = open('poem.txt')# если не указан режим, по умолчанию подразумевается
                    # режим чтения ('r'eading)

while True:
    line = f.readline()
    if len(line) == 0:# Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

f.close()# закрываем файл

import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)# помещаем объект в файл
f.close()

del shoplist# уничтожаем переменную shoplist

try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))

class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки -- {0}; \
ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений.')

import time

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    print('(Очистка: Закрытие файла)')

with open("poem.txt") as f:
    for line in f:
        print(line, end='')

import sys
sys.version_info
sys.version_info[0] >= 3

import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы необходима как минимум \
                    версия Python 3.0", RuntimeWarning)
else:
    print('Нормальное продолжение')

import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
        os.getenv('HOMEPATH'), \
        'test.log')

else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print("Сохраняем лог в", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")

def get_error_details():
    return (2, 'описание ошибки No2')
errnum, errstr = get_error_details()

print(errnum, errstr)

a, *b = [1, 2, 3, 4]

print(a, '\n', b)

a = 6
b = 9
a, b = b, a
print(a, b)

flag = True
if flag:
    print('Yes')

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

def powersum(power, *args):
    '''Возвращает сумму аргументов, возведённых в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

powersum(2, 3, 4)
powersum(2, 10)

exec('print("Здравствуй, Мир!")')
eval('2*3')

mylist = ['item']
assert len(mylist) >= 1

print(mylist.pop())
print(mylist)

i = []
i.append('item')

print(repr(i), eval(repr(i)), eval(repr(i)) == i)

class Abbr(object):
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

print(Abbr())

a = """А давайте поиграем в Крестики и Нолики (но я советвою позвать вашем друга чтобы месте играть)
[бот не создан]"""
print(a)

import tic_tac_top_2D

print("\nпрочитайте стих от один, из разрабочитка питон\n")

import this

print('\nИ ещё кода из других файл tasks.py и Neural_network.py\n')

import Neural_network
print('\n')
import tasks

print("\nДо Свидания\nПриходите Еще Раз\n")

print("15 6\n5 21 14 1 11\n16 20\n20 16 14\n25 20 16\n23\n20 21 20\n\tшифор ATЯ33")
print("@Yura_Mukhin")
input("Нажми ENTER чтобы закончить код: ")