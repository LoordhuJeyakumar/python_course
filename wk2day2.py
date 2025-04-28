# Tuple creation
student_info= ("Rakshi", 20, "Computer science")
print("Student details:", student_info)
print("Student's name:", student_info[0])
print("Student's major:", student_info[-1])

# packing and unpacking

values=(100, 200, 300)
x,y,z = values
print(x, y, z)
# or
print("x:", x)
print("y:", y)
print("z:", z)

# set creation

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("set1:", set1)
print("set2:", set2)

set1.add(6)
print(set1)
set2.discard(2)
print(set2)
set2.remove(1)
print(set2)

#Set operation

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1 | set2  
print("Union:", union)
intersection = set1 & set2 
print("Intersection:", intersection)
difference = set1 - set2 
print("Difference (set1 - set2):", difference)
symmetric_difference = set1 ^ set2  
print("Symmetric Difference:", symmetric_difference)
is_subset = set1 is_subset(set2)
print("set1 is a subset of set2:", is_subset)