def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Prabha")
greet_person("Priya")

2
import math
def calculate_circle_area(radius):
    return math.pi * radius* radius
radius = 5
area = calculate_circle_area(radius)
print(f"The area of circle radius {radius} is {area:.2f}")

3
def describe_product(name, price, category):
    print(f"product: {name}, price: ${price:.2f}, category: {category}")

describe_product(category="Kitchen appliance", price=5000, name="mixer")                 
describe_product(category="Home appliances", price=10000, name="SOfa")

4
def send_email(recipient_email, subject, body="No message body provided."):
    print(f"To: {recipient_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    send_email("best@example.com", "Python Class Reminder")
    send_email("example@examplel.com", "Complete the task EOD")

5
global_message ="Hello from global scope"
def scope_test():
    print(global_message)

    local_message = "Hai from local scope"
    print(local_message)

    scope_test()

    try:
       print(local_message)
    except NameError as e:
        print(f"Error: {e}")
    def scope_test_modified():
        global global_message
        global_message ="Message changed inside function"
        print(global_message)
        scope_test_modified()  
        print(global_message)