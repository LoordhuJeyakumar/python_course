#tuple

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

# 
tuple2 = tuple('hello')
print(tuple2)

#mixed tuple
tuple3 = (1, 2, 3, 'a', 'b', 'c', True, 3.14, "Python")
print(tuple3)

single_item_tuple = (5,) # Note the comma!
print(single_item_tuple) # Output: (5,)
print(type(single_item_tuple)) # Output: <class 'tuple'>

#tuple packing and unpacking
tuple4 = 1, 2, 3, 4, 5
print(tuple4)
print(type(tuple4))

#tuple unpacking
a, b, c, d , e = tuple4
print(a)
print(b)
print(c)
print(d)
print(e)


#tuple constructor
tuple5 = tuple([1, 2, 3, 4, 5])
print(tuple5)
print(type(tuple5))


#tuple indexing and slicing
tuple6 = (1, 2, 3, 4, 5)    
print(tuple6[0]) # Output: 1
print(tuple6[-1]) # Output: 5
print(tuple6[1:4]) # Output: (2, 3, 4)
print(tuple6[:3]) # Output: (1, 2, 3)
print(tuple6[2:]) # Output: (3, 4, 5)
print(tuple6[::2]) # Output: (1, 3, 5)

#tuple immutability
tuple7 = (1, 2, 3, 4, 5)
#tuple7[0] = 10 # TypeError: 'tuple' object does not support item assignment (cannot change item)
#tuple7.append(6) # AttributeError: 'tuple' object has no attribute 'append' (no methods to add/remove items)


#tuple methods
tuple8 = (1, 2, 2, 3, 2, 4)
print(tuple8.count(2)) # Output: 3  
print(tuple8.index(3)) # Output: 3

