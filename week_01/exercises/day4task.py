number = int(input("Enter the value"))
if number>0:
    print("The number is positive:")
elif number<0:
    print("The number is negative:")
else:
    print("zero")

number = int(input("enter the integer"))
if number%2==0:     
   print("even")
else:
   print("odd")

number1 = int(input("enter the num"))
number2 = int(input("enter the num"))
if number1>number2:
    print("number1 is greater")
elif number2>number1:
    print("number2 is greater")
else:
   print("numbers are equal")

score = int(input("Enter your score"))
if score<100 and score>=90:
    print("A+")
elif score>=80 and score<=89:
    print("A")
elif score>=70 and score<=79:
    print("B+")
elif score>=60 and score<=69:
    print("C")
else:
    print("fail")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

age = int(input("Enter the age:"))
if age<=18:
    print("Not Eligible for vote")
else:
    print("Eligible for vote")


 


