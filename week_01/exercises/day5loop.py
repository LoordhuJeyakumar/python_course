sum = 0
for i in range(1,11):
    sum+=i
print(f"Total value is:{sum}")


factorial = 1
number =int(input("Enter the value:"))
for i in range (1, number+1):
    factorial=factorial*i
    print(factorial)


num = int(input("Enter a number: "))
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


number = int(input("Enter an number: "))
count = 0
if number == 0:
    count = 1
else:
 while number != 0:
        number //= 10  
        count += 1   
print("Number of digits:", count)



while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("entered number is low, Try again.")
    elif guess > number:
        print("enterted number is high, Try again.")
    else:
        print("Correct")
        break
number = 1
while number <= 5:
    print(number)
    number += 1 