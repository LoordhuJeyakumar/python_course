#list 
#list syntex

# list1 = [1, 2, 3, 4, 5]
# print(list1)

# list2 = ['a', 'b', 'c', 'd', 'e']
# print(list2)    


# list3 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']    
# print(list3)


# # constructor
# list4 = list()
# print(list4)

# list5 = list([1, 2, 3, 4, 5])
# print(list5)


# # list methods
# fruits = ['apple', 'banana', 'cherry']
# print(fruits)

# print(fruits[0])

# #lenth 
# print(len(fruits))

#List methods

# fruits = ['apple', 'banana', 'cherry', 'date']

# print(fruits)

# fruits.append('mango')

# print(fruits)

# fruits.insert(3, 'kiwi')

# print(fruits)

# fruits.remove('banana')

# print(fruits)

# fruits.pop(2)

# print(fruits)

# fruits.clear()

# print(fruits)

""" fruits = ['date','apple', 'banana', 'cherry', 'mango','kiwi','orange', "Apple",'apple' ]

print(fruits)

fruits.sort()

print(fruits)

fruits.reverse()

print(fruits)

print(fruits.index('date'))

print(fruits)

print(fruits.count('Apple'))

print(fruits) """



#list slicing

# fruits  = ['date','apple', 'banana', 'cherry', 'mango','kiwi','orange', "Apple",'apple' ]

# print(f"Normal list:{fruits}")


# print(f"List slicing 0 to 3:{fruits[0:3]}")

# print(f"List slicing 3 to 6:{fruits[3:6]}")

# print(f"List slicing 6 to end:{fruits[6:]}")

# print(f"List slicing start to end:{fruits[:]}")

# print(f"List slicing start to end with step 2:{fruits[::2]}")

# print(f"List slicing start to end with step 3:{fruits[::3]}")

# print(f"List slicing start to end with step 4:{fruits[::4]}")


# #list unpacking

# numbers = [1, 2, 3, 4, 5]

# a, b, c, d, e = numbers

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# print("=================")

# #list unpacking with * operator 

# numbers = [1, 2, 3, 4, 5]

# a, b, c, d, *e = numbers

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# print("=================")

#list methods

#del

# numbers = [1, 2, 3, 4, 5]

# #del numbers[2]

# print(numbers)

# print("=================")

# del numbers[0:2]

# print(numbers)

#List operations

# numbers = [1,2,3]

# numbers2 = [1, 3, 5, 7, 9]

# numbers3 = numbers + numbers2

# #print(numbers3)

# numbers4 = numbers * 4

# print(numbers4)

# numbers5 = [1, 2, 3, 4, 5]

# numbers5[2] = 10

# print(numbers5)


# numbers = [1, 2, 3, 4, 5]


# #Shallow Copy

# numbers = [1, 2, 3, 4, 5]

# numbers2 = numbers.copy()

# numbers[2] = 10

# print(numbers)

# print(numbers2)

# #Deep Copy

# numbers = [1, 2, 3, 4, 5]

# numbers2 = numbers[:]

# numbers[2] = 10

# print(numbers)

# print(numbers2) 