#file handling

#paths
 #1.absolute path
#C:\Users\john\OneDrive\Desktop\Python_Course\week_03.5\exercises\numbers.txt

 #2.relative path

# import os

# current_dir = os.getcwd()
# print("Current working directory:", current_dir)

#file handling

""" 
+---------------+
|   Start       |
+---------------+
        |
        v
+-----------------------+
| Open the file (mode)  |
+-----------------------+
        |
        v
+-------------------------+
| Process file (read/write) |
+-------------------------+
        |
        v
+-----------------------+
|      Close file       |
+-----------------------+
        |
        v
+---------------+
|     End       |
+---------------+

 """

#opeining the file
file_path = "numbers.txt"

# file_object = open(file_path, "r")

# #processing the file

# print(file_object.read())

# file_object.close()


""" file_object = open(file_path, "w")

file_object.write("Hello World")

file_object.close() """
""" 
file_object = open(file_path, "a")

lst = [1,"\n",2,"\n",3,"\n",4 , "\n",5]

for item in lst:
    file_object.write(str(item))

file_object.close()
 """

""" file_object = open(file_path, "w")

quot_list = [
    "Life is what happens when you're busy making other plans.\n",    
    "Get busy living or get busy dying.\n",
    "You have to do something to keep yourself busy.\n",
    "Life is either a daring adventure or nothing at all.\n", 
    "Life is 10% what happens to you and 90% how you react to it.\n"
]

for item in quot_list:
    file_object.write(item) 

file_object.close() """

    
""" file_object = open(file_path, "r")

line = file_object.read()
print(file_object.tell())

print(line)
file_object.seek(10)
print(file_object.read()) """

# file_object = open(file_path, "r")

# lines_list = file_object.readlines()

# print(lines_list)

""" with open(file_path, "r") as file_object:
    lines_list = file_object.readlines()
    print(lines_list)
    print(file_object.tell())
    file_object.close()


print(file_object.read()) """

""" file_object = open("new_file_2.txt", "x")

file_object.write("Hello World, from another file 2")

file_object.close """

""" binary_data = b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21' # Bytes representing "Hello, world!"
try:
    file = open("binary_output.bin", 'wb') # Open in write binary mode
    file.write(binary_data) # Write bytes object
    print("Binary data written to 'binary_output.bin'")
finally:
    file.close() """

#Context Manager for file handling

#syntax

""" with open(filename, mode, encoding=...) as file_objectt: """

# try:
#     with open("numberss.txt", 'r', encoding='utf-8') as file: # Open file using 'with'
#         print(file.closed)
#         content = file.read() # Read content within the 'with' block
#         print("--- File Content (using 'with') ---")
#         print(content)
#         print("--- End of Content ---")
#     # File is automatically closed here when exiting 'with' block
    
#     print("File has been automatically closed.")
# except FileNotFoundError:
#     print("Error: File not found!")
# except Exception as e:
#     print(f"An error occurred: {e}")


#print(file.closed)

# mode r+

try:
    with open("numbers.txt", 'r+', encoding='utf-8') as file: # Open file using 'with'
        print(file.closed)
        content = file.read() # Read content within the 'with' block
        print("--- File Content (using 'with') ---")
        print(content)
        print("--- End of Content ---")
        file.write("Hello World")
        print(file.read())
    # File is automatically closed here when exiting 'with' block

    print("File has been automatically closed.")
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
    print(file.closed)