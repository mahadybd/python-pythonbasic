# a = 'Hello World'
# print(a)

# string
# name = 'Mahady'
# age = 34

# print(f'My Name is {name} and i am {age}')

# capitalize string
# s = 'hello world'
# # print(s.swapcase())
# print(s.split())

# ------List --------------
# numbers = [1, 2, 3, 4, 5]
# numbers2 = list((1, 2, 3, 4, 5)) # same results as numbers
# fruits = ["apple", "Oranged", "Grapes"]
# print(fruits[1]) # Oranged
# print(fruits[-1]) # Grapes
# print(fruits[0:2])
# fruits.remove("apple")
# print(fruits)
# # fruits.append("Mango")
# fruits.insert(2, "Strawberries")
# fruits.pop(2)
# fruits.sort()
# fruits.sort(reverse=True)
# fruits[0] = "Blueberries"
# print(fruits)
#-----------------------
# healthy = ["kale chips", "broccoli"]
# backpack = ["pizza","frozen custard", "apple crisp", "kale chips"]

# print(backpack)
# [:] slice --> keeps same object id . in memory, old backpack will replace.
# backpack[:] = [item for item in backpack if item in healthy]

# print(backpack)

# same result with for loop.............
# healthy_backpack = []

# for item in backpack:
#     if item in healthy:
#         healthy_backpack.append(item)

# print(healthy_backpack)
#------------------------
# squares = []

# for i in range(10):
#     squares.append(i ** 2)

# print(squares)

# same result-----------
# squares2 = [i ** 2 for i in range(10)]
# print(squares2)

# squares3 = [i ** 2 for i in range(10) if i % 2 == 0]
# print(squares3)
#--------------------------
# greetings = ["hi", "hello", "hallo","wassap","yo"]

# for i in range(len(greetings)):
#     print(i, greetings[i])
#--------------------------
# backpack = ["pizza","frozen custard", "apple crisp", "kale chips","pizza", "pizza"]

# count = [[backpack.count(item), item] for item in  set(backpack)]
# print(count)
#--------------------------
from collections import Counter

fruits = ["apple", "Oranged", "Grapes","apple", "Oranged", "Grapes", "banana","apple", "Oranged", "Grapes",]

print(Counter(fruits)) # return dictionary . this is the best way to count a list
# (printed result)-> Counter({'apple': 3, 'Oranged': 3, 'Grapes': 3, 'banana': 1})

# ------Tuple --------------
# Tuple ordered and unchangeable. allow duplicate value
# fruits = ("apple", "Oranges", "Grapes")
# fruits2 = ("Apple",)  # single tuple
# del fruits2

# numbers = (1,2,3,4,4,5)
# print(numbers.count(4))
# print(numbers.index(4))

# ------Set ------------------------
# unordered and unindexed. No duplicate members
# fruits_set = {"apple", "Oranged", "Grapes"}

# print("apple" in fruits_set)  # return true or false

# fruits_set.add('Blueberries')
# fruits_set.remove('apple')
# fruits_set.clear()
# del fruits_set
# print(fruits_set)

# ------ Dictionary --------------
# unordered, unchangeable and indexed. No duplicate members

# person = {
#     'first_name': 'Mahady',
#     'last_name': 'Hasan',
#     'age': 30
# }
# print(person['first_name'])
# print(person.get('last_name'))  # get value with get method

# person['phone'] = '012546987'
# print(person)

# person2 = person.copy()
# person2['city'] = 'Chemnitz'
# print(person2)

# del(person['age'])  # remove item
# person.pop('phone')  # remove item
# print(person)
# person.clear()

# list of dict
# people = [
#     {'name': 'Afruja', 'age': 35},
#     {'name': 'ANHA', 'age': 4},
#     {'name': 'Mahady', 'age': 35},
#     {'name': 'Ayra', 'age': 2}
# ]

# print(people[1]['name'])

# --------- function --------------
# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

# create function--------
# def printName(name='Hasan'):
#     print(f'Hello {name}, I am a function')


# printName('Mahady Hasan')

# Return values--------


# def getSum(num1, num2):
#     total = num1 + num2
#     return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# getSum = lambda num1, num2: num1 + num2


# print(getSum(10, 3))

#---[ The range Function ]

# numbers = range(5, 10, 2)
# # print(numbers) # range(0, 5)
# for number in numbers: 
#     print(number)

# --------- Conditionals --------------
# x = 5
# y = 50

# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}') 

# #nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')


#conditional operators (and, or, not)---------
# if not(x == y):
#     print(f'{x} is not equal to {y}')

# (is not) (not in) condition----------
# numbers =[10,20,30,40,50]

# if x not in numbers:
#     print( f' {x not in numbers} from not in contion')
# elif x is not y:
#     print(f'{x is not y} from is not condition')


# For loop ---------
# people = ['Mahady', 'Hasan', 'Anha','Ayra','Afruja']

# for person in people:
#     if person =='Ayra':
#         break
#     print(f'Current person: {person}')

# range------

# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Number {i}')

# While loop------
# count = 0
# while count < 10:
#     print(f'Count: {count}')
#     count += 1

# --------- Arithmetic Operators ----------

# print(10 / 3) #3.3333333333333335
# print (10//3) #3 integer value only
# print (10 ** 3) # 1000 # 10 power of 3
# print( 10 % 3) # 1

# x = 10 + 3 * 2 #16
# y = (10 + 3) * 2 # 26

# print(x,y)

# ---------Type Conversion----------

# birth_year = '1984'
# age = 2022 -int(birth_year)
# print(age)

# first = input('First: ')
# second = input('Second: ')
# # sum = int(first) + int(second)

# print(sum)
# # print( 'Sum is:' + str(sum) )
# # print(f'Sum is: {sum}')