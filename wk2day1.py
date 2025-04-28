programming_languages = ["Python","Java","Javascript","C++"]
print("Programming languages list:",programming_languages)
print(programming_languages[0])
print(programming_languages[2])
print(programming_languages[-1])

#List modification

numbers=[1, 2, 3, 4, 5]
print("Numbers list:", numbers)
numbers[1]=10
print("Number 1 changed:", numbers )
numbers.append(6)
print("Adding number 6:", numbers)
numbers.insert(0, 0)
print("Inserting 0:", numbers)
numbers.remove(4)
print("Number 4 removed:", numbers)

# list filtering and transformation
numbers=[1, 5, 12, 3, 18, 22, 7, 30]
even_numbers=[]
for num in numbers:
    if num % 2 == 0:
       even_numbers.append(num)
squared_numbers=[]
for num in numbers:
    squared_numbers.append(num**2)
    print("Even:", even_numbers)
    print("square:", squared_numbers)

#list method

colors = ["red", "green", "blue", "red", "yellow", "red"]
count_red= colors.count("red")
print(f"Count of red: {count_red}")
index_blue=colors.index("blue")
print(f"index of blue: {index_blue}")
colors.sort()
print("sorting the colors:", colors)
colors.reverse()
print("Reversed colors:", colors)
colors_copy = colors.copy()
colors_copy.append('purple')
print("color 1:", colors)
print("color 2:", colors_copy)

# list slicing
letters =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
five_element=letters[:5]
print("five_elements:", five_element)
sublist_3to7=letters[3:7]
print("element from 3 to 7", sublist_3to7)
second_element=letters[::2]
print("every second element:", second_element)
reversed_element=letters[::-1]
print("list in reverse order:", reversed_element)
last_3 = letters[-3:]
print("last 3 elements from list:", last_3)
