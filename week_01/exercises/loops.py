# loops

# for loop

message = "Hello World, Hello Python"

# for char in message:
#     char.upper()
#     print(char)

# range loop

for i in range(5):
    print(i)

print("\n ++++++ \n")
print("range(2, 7)")
for i in range(2, 7):
    print(i)

print("\n ++++++ \n")
print("range(2, 7, 2)")
for i in range(2, 7, 2):
    print(i)

# step loop

print("\n ++++++ \n")
print("range(7, 2, -1)")
for i in range(7, 2, -1):
    print(i)


# else statement in for loop

print("\n ++++++ \n")
for i in range(5):
    print(i)
else:
    print("Loop finished")


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Found 3!")
        break # Loop terminates here
    print(num)
else: # This else block will NOT execute because the loop was terminated by 'break'
    print("Loop completed normally")


# while loop

count = 0

while count < 5:
    print("Count is:", count)
    count += 1

print("\n ++++++ \n")

count = 0

# Using while loop to get valid user input (example):
# user_input = ""
# while user_input.lower() != "quit": # Loop until user types "quit" (case-insensitive)
#     user_input = input("Enter command (or 'quit' to exit): ")
#     print("You entered:", user_input)


# print("Exiting program.")


# Nested loops

for i in range(3):
    for j in range(4):
        print(f"i={i}, j={j}")

print("\n ++++++ \n")

for i in range(3):
    for j in range(4):
        print("*", end=" ") # Print a star and a space, end=' ' keeps output on the same line
    print() # Move to the next line after each row is printed

print("\n ++++++ \n")

# else statement in while loop

count = 0

while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("While loop condition became false, loop ended.")


count = 0

while count < 5:
    print("Count is:", count)
    if count == 2:
        break
    count += 1
else:
    print("While loop condition became false, loop ended.")



# loop control statements

print("\n ++++++ control statements \n")
for i in range(5):
    if i == 2:
        continue # Skip the rest of the loop body for this iteration
    print(i)

print("\n ++++++ \n")
for i in range(5):
    if i == 2:
        break # Exit the loop entirely
    print(i)

print("\n ++++++ \n")
for i in range(5):
    print(i)
    if i == 2:
        break

print("\n ++++++ \n")
for i in range(5):
    if i == 2:
        pass # Do nothing, acts as a placeholder
    print(i)



