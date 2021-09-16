# weight = float(input('Enter your weight: '))
# unit = input('Enter k for kg or l for pound: ').upper()
#
# if unit == "K":
#     print('Your weight in pound is:', weight*2.20462)
# else:
#     print('your weight in kg is:', weight/2.20462)

# course = 'Python'
# print(course[1:-1])
# first = 'Haseeb'
# last = 'shah'
# msg = f'{first} [{last}] is a coder'
# print(msg)
# import random

# weather = input('''what's the weather "condition" in your are
# enter 'hot' 'cold' or 'lovely' accordingly: ''')

# hot = False
# cold = True
#
# if hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print('you are good?')


# price = 1000000
# credit = True
# income = True
#
# var = 5 != 5
#
# if 5==4:
#     print('Down Payment is $', price*0.1)
# else:
#     print('Down payment is $', price*0.2)


# name = input('''Enter user name
# username must be 3-50 ch:''')
# if len(name) < 3:
#     print('name must be at least 3 ch')
# elif len(name) > 50:
#     print('name must be of 50 ch')
# else:
#     print('name is good')
import random

# count = 1

# while count<=10:
#     # if i==5:
#     #     print('Five occured')
#     # else:
#     # print((10 - i) * ' ' + i*'*')
#     y=1
#     while y<=10-count:
#         print('1',end='')
#         y+=1
#     x= 1
#     while x<=count:
#         print('*',end = '')
#         x+=1
#     print()
#     count+=1
#
# print('Number %.2f' %1.5)

# secret = random.randrange(1, 10)
# print(secret)
# count = 0
#
# while count < 3:
#     guess = input('Enter Guess: ')
#     if int(guess) == secret:
#         print('You won!!!')
#         break
#     print('Try again !!!')
#     count += 1
#
# if count == 3:
#     print('Better Luck next Time')
#     print("Number was", secret)

# input(">")
# print(''' Start --- start the car
#  Stop --- stop the car
#  Quit --- to exit''')
#
# start = False
# stop = True
# while True:
#     user_action = input(">")
#     if start and user_action.lower() == 'start':
#         print(" Car is already started")
#         continue
#     if stop and user_action.lower() == 'stop':
#         print(" Car is already stopped")
#         continue
#     if user_action.upper() == 'START':
#         print(" Car Started")
#         start = True
#         stop = False
#     elif user_action.lower() == 'stop':
#         print(" Car is stopped")
#         start = False
#         stop = True
#     elif user_action.lower() == 'exit':
#         break
#     else:
#         print("Action is not understand")
#
# print("Thanks for riding")

# sum = 0
# for object in [10, 20, 30]:
#     sum += object
# print(f"Total is: {sum}")
#
# for i in range(10):
#     print(i)

# number = [1, 2, 3, 4, 5]
#
# for i in number:
#     for y in range(i):
#         print("x", end='')
#     print()
# print()
# for i in number:
#     print('x' * i)

# height = int(input('Enter the height of peramit: '))
# for i in range(1, height+1, 2):
#     # print(' ' * ((height-i)//2), end='')
#     # print('*' * i, end='')
#     print()
#     for s in range((height-i)//2):
#         print(' ', end='')
#     for x in range(i):
#         print('*', end='')

# array = ['jon', 5, 'local', 'kilo', 5.4]
# print(array[:])
#
# print(type(array[len(array)-1]))

# d2_array = [[5, 6, 7], [5, 8, 9], [7, 6, 8]]
#
# largest = d2_array[0][0]
# smallest = d2_array[0][0]
#
# d2_array[random.randrange(0, len(d2_array))][random.randrange(0, 2)] = random.randrange(4, 11)
# for array in d2_array:
#     for item in array:
#         if item > largest:
#             largest = item
#         elif item < smallest:
#             smallest = item
#
# print(f'Largest element is {largest}. Smallest element is {smallest}.')

# table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# turn = 'O'
# counter = 0
# status = None
# while True:
#     counter += 1
#     for row in table:
#         for element in row:
#             print(f'| {element} ', end='')
#         print()
#         print('----'*3)
#
#     if status == 1:
#         break
#
#     while True:
#         print("Enter location to place your selection: ")
#         row = int(input('Row '))
#         column = int(input('Column '))
#
#         if (table[row][column] == 'O') or (table[row][column] == 'X'):
#             print('Location is already selected re-select the location.')
#             continue
#         table[row][column] = turn
#         if counter % 2:
#             turn = 'X'
#         else:
#             turn = 'O'
#         break
#
#     if counter >= 5:
#         for i in range(3):
#             if table[i][0] == table[i][1] == table[i][2]:
#                 if table[i][0] == 'O':
#                     print('player 1 won')
#                     status = 1
#                     break
#                 else:
#                     print('player 2 won')
#                     status = 1
#                     break
#
#         for y in range(3):
#             if table[0][y] == table[1][y] == table[2][y]:
#                 if table[0][y] == 'O':
#                     print('player 1 won')
#                     status = 1
#                     break
#                 else:
#                     print('player 2 won')
#                     status = 1
#                     break
#
#         if table[0][0] == table[1][1] == table[2][2]:
#             if table[0][0] == 'O':
#                 print('player 1 won')
#                 status = 1
#             else:
#                 print('player 2 won')
#                 status = 1
#
#         if table[0][2] == table[1][1] == table[2][0]:
#             if table[0][2] == 'O':
#                 print('player 1 won')
#                 status = 1
#             else:
#                 print('player 2 won')
#                 status = 1
# list = [1, 2, 3, 3, 5, 4, 6, 6, 7]
# # list.clear()
# list.append(4)
# # list.pop()
# list.insert(1, 5)
# list.sort()
# list.reverse()
# print(list)

# for i in list:
    # print(list.count(i))
    # count = list.count(i)
#     if count > 1:
#         for x in range(count-1):
#             list.remove(i)
#
# list.sort()
# print(list.count(1))

# unique = []
# for num in list:
#     if num not in unique:
#         unique.append(num)
#
# print(unique)

# cordinates = (1, 2, 3)
# x, y, z = cordinates
# print(cordinates.count(3))

# dictionary = {
#     ":)": "😊",
#     ":(": "😥"
# }
# # dictionary.clear()
# # dictionary.popitem()
# dictionary["a_a"] = "🤨"
#
# msg = input("Enter Msg: ")
# words = msg.split(" ")
# out = ""
# for word in words:
#     out += dictionary.get(word, word) + " "
# print(out)

# number = int(input("Enter number to get table: "))
#
# def table( num ):
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num*i}")
#
# table(number)


# msg = input("Enter message: ")
#
#
# def emoji_converter(msg):
#     dictionary = {
#         ":)": "😀",
#         ":(": "😥"
#     }
#     words = msg.split(" ")
#     out = ""
#     for word in words:
#         out += dictionary.get(word, word) + " "
#
#     return out
#
#
# try:
#     print(emojiConverter(msg))
# except:
#     print('Not define')

# import math
#
# class Circle:
#     radius = 0
#     def __init__(self, radius):
#         self.radius = radius
#
#     def diameter(self):
#         return self.radius*2
#
#     def area(self):
#         return math.pi*(self.radius**2)
#
#     def circumference(self):
#         return math.pi*2*self.radius

import learning.random
# from learning import random
# try:
# c = Circle()
# c.radius = 5
# print(f"Diameter: {c.diameter()}, Area: {c.area()}, Circumference: {c.circumference()}")
# print("Area %.f" %c.area())
# except :
#     print("error")
# print(learning.random.select_leader(('zain', 'shane', 'jane')))

# class Shape(Circle):
#     def name(self):
#         print("Dead")
#
#
# s = Shape()
# print(s.area())

# print(learning.random.square(5))


