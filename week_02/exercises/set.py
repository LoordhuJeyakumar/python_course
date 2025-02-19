#set data structure

set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))

my_set = {1, 2, 3, 2, 4} # Duplicate '2' will be automatically removed
print(my_set) # Output: {1, 2, 3, 4} (order may vary)
print(type(my_set)) # Output: <class 'set'>

string_set = {"apple", "banana", "apple", "orange"} # Duplicate "apple" removed
print(string_set) # Output: {'banana', 'apple', 'orange'} (order may vary)

#empty set
empty_set = set()
print(empty_set) # Output: set()
print(type(empty_set)) # Output: <class 'dict'> (not a set)



my_list = [1, 2, 2, 3, 4, 4, 4]
set_from_list = set(my_list) # Remove duplicates
print(set_from_list) # Output: {1, 2, 3, 4}

set_from_string = set("Mississippi") # Unique characters from the string
print(set_from_string) # Output: {'M', 'i', 's', 'p'} (order may vary)

#using tuple
tuple1 = (1, 2, 3, 4, 4, 4)
set_from_tuple = set(tuple1) # Remove duplicates
print(set_from_tuple) # Output: {1, 2, 3, 4}

print("Operations")
#set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # Union of two sets

print(union_set) # Output: {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2) # Intersection of two sets
print(intersection_set) # Output: {3}


difference_set = set1.difference(set2) # Difference between two sets    
print(difference_set) # Output: {1, 2}

symmetric_difference_set = set1.symmetric_difference(set2) # Symmetric difference between two sets
print(symmetric_difference_set) # Output: {1, 2, 4, 5}


#set methods
set1 = {1, 2, 3}
set1.add(4) # Add an element to the set
print(set1) # Output: {1, 2, 3, 4}
set1.remove(2) # Remove an element from the set
print(set1) # Output: {1, 3, 4}
set1.discard(3) # Remove an element from the set if it exists
set1.discard(10) # No error if the element doesn't exist
print(set1) # Output: {1, 4}
set1.clear() # Remove all elements from the set
print(set1) # Output: set()

#update 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2) # Update set1 with elements from set2
print(set1) # Output: {1, 2, 3, 4, 5}

removed = set1.pop() # Remove and return an arbitrary element from the set
removed2 = set1.pop() # Remove and return another arbitrary element from the set
print(set1) # Output: {2, 3, 4, 5}
print(removed) # Output: 1 (the removed element)
print(removed2) # Output: 2 (the removed element)

set1 = {1, 2, 3, 4, 5}

print(len(set1))

#copy
setCopy = set1.copy()
print(setCopy)
#set comprehension
set1 = {x for x in range(5)}
print(set1) # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}