# """ class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number # Public attribute
#         self._balance = balance          # "Private" attribute (by convention)

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Deposit amount must be positive.")

#     def get_balance(self): # Public method to access balance
#         return self._balance
    

# account = BankAccount("123456", 1000)
# account.deposit(500)
# print(account.get_balance())

# #check private attribute
# print(account._balance )#bad practice

# #change private attribute
# account._balance = 2000

# print(account.get_balance())#good practice

# #getter and setter

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self._balance = balance


# account = BankAccount("123456", 1000)

# account.balance = 2000
# print(account.balance)

# account.balance = -500
# print(account.balance) """



# #procedural programming or sequential programming
# """ def create_account(account_number, balance):
#     return {"account_number": account_number, "balance": balance}


# def deposit(account, amount):
#     if amount > 0:
#         account["balance"] += amount
#     else:
#         print("Deposit amount must be positive.")


# def get_balance(account):
#     return account["balance"]


# account = create_account("123456", 1000)
# print(account)
# deposit(account, 500)
# print("after deposit", account)
# print(get_balance(account))


# acount_1 = create_account("1234567", 1000)
# acount_2 = create_account("1234568", 1000)

# deposit(acount_1, 500)
# deposit(acount_2, 500)

# print(get_balance(acount_1))
# print(get_balance(acount_2)) """

# # procedural programming or sequential programming

# no_of_wheels = 4    
# color = "blue"
# no_of_airbags = 2
# milage = 10000
# top_speed = 200

# def drive():
#     print("Driving the car")

# def  stop():
#     print("Stopping the car")

# def move():
#     drive()
#     stop()


# car_2_no_airbags = 5

# """ 
# class Car:
#     no_of_wheels = 0
#     color = ""
#     no_of_airbags = 0
#     milage = 0
#     top_speed = 0

#     def drive(self):
#         print("Driving the car")

#     def stop():
#         print("Stopping the car")

  


# car_1 = Car()

# car_1.no_of_wheels = 4
# car_1.color = "blue"
# car_1.no_of_airbags = 2
# car_1.milage = 10000    
# car_1.top_speed = 200

# print('Car_1', car_1.no_of_wheels, car_1.color, car_1.no_of_airbags, car_1.milage, car_1.top_speed)

# car_2 = Car()

# car_2.no_of_wheels = 4
# car_2.color = "red"
# car_2.no_of_airbags = 4
# car_2.milage = 1000    
# car_2.top_speed = 100

# print('Car_2', car_2.no_of_wheels, car_2.color, car_2.no_of_airbags, car_2.milage, car_2.top_speed)

# car_3 = Car()

# car_3.no_of_wheels = 4
# car_3.color = "blue"
# car_3.no_of_airbags = 2
# car_3.milage = 10000    
# car_3.top_speed = 200

# print('Car_3', car_3.no_of_wheels, car_3.color, car_3.no_of_airbags, car_3.milage, car_3.top_speed)

# car_1.drive() """


# class Car:
    
# #constructor
#     def __init__(self):
#         #print("Constructor called for", self)
#         self.brand = ""
#         self.color = ""
#         self.milage = 0
#         self.top_speed = 0

#     def drive(self, km):
#         print("Driving the car for", km, "km")

#     def stop(self):
#         print("Stopping the car")

#     def move(self):
#         self.drive()
#         self.stop()

# new_car = Car()
# new_car.brand = "BMW"
# new_car.color = "red"
# new_car.milage = 1000

# benz = Car()
# benz.brand = "Mercedes"
# benz.color = "black"
# benz.milage = 2000

# new_car.drive(100)

# email_data = [
#     {
#         "sender": "john@example.com",
#         "recipient": "jane@example.com",
#         "subject": "Hello",
#         "body": "Hi there!"
#     },
#     {
#         "sender": "jane@example.com",
#         "recipient": "john@example.com",
#         "subject": "Hi",
#         "body": "Hey!"
#     }

# ]


# class EmailService:
#     def __init__(self, sender, recipient, subject, body):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body
    
#     def send_email(self):
#         print("Sending email to", self.recipient)
#         print("Subject:", self.subject)
#         print("Body:", self.body)

#     def send_bulk_email(self, emails):
#         for email in emails:
#             self.sender = email["sender"]
#             self.recipient = email["recipient"]
#             self.subject = email["subject"]
#             self.body = email["body"]
#             self.send_email()



# #send bulk email
# email_service = EmailService("", "", "", "")
# email_service.send_bulk_email(email_data)



# class Car :
#     #constructor
#     def __init__(self, brand, color, milage, top_speed):
#         self.brand = brand
#         self.color = color
#         self.milage = milage
#         self.top_speed = top_speed

#         #print("Constructor called for", )
        

#     #destructor
#     # def __del__(self):
#     #     print("Destructor called for", self.brand)
    
#     #String representation
#     def __str__(self):
#         return self.brand
    
#     def move(self):
#         print("Driving the car")

#     def stop(self):
#         print("Stopping the car")
    



# car1 = Car("BMW", "red", 1000, 200)
# car2 = Car("Mercedes", "black", 2000, 300)

# # print(car1.brand, car1.color, car1.milage, car1.top_speed)
# # print(car2.brand, car2.color, car2.milage, car2.top_speed)

# print(car1.color)S
# from Car import Car

# # Parameters
# #  make
# #  model
# #  year
# #  color
# #  milage
# #  top_speed

# car1 = Car("BMW", "X5", 2020, "red", 1000, 200)
# car2 = Car("Mercedes", "C63", 2021, "black", 2000, 300)

# car1.__no_of_wheels = 10

# print(car1.__no_of_wheels)

# print(car1.get_no_of_wheels()) # > default value of no_of_wheels is 4
# car1.set_no_of_wheels(15) # > set car1 no_of_wheels to 15

# print(car1.get_no_of_wheels()) # > 15

# car2.get_no_of_wheels() # > default value of no_of_wheels is 4

# print(car2.get_no_of_wheels()) # > default value of no_of_wheels is 4

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number # Public attribute
#         self.__balance = balance          # "Private" attribute (by convention)


#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Deposit amount must be positive.")

#     def get_balance(self): # Public method to access balance
#         return self.__balance
    

# account_1 = BankAccount("123456", 1000)
# account_1.deposit(500)
# account_1.__balance = 10000
# print(account_1.get_balance())


# account_2 = BankAccount("789123", 2000)


class Swap:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._temp = None

    def swap(self):
        self._temp = self.a
        self.a = self.b
        self.b = self._temp
        return self.a, self.b
    


swap = Swap(1, 2)
print(swap.swap())

   