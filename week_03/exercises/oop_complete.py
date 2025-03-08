from abc import ABC, abstractmethod

# -----------------------------
# Abstraction and Inheritance
# -----------------------------

class MenuItem(ABC):
    """
    Abstract class for menu items.
    """
    def __init__(self, name:str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self):
        """
        Abstract method to get the details of the menu item.
        """
        pass

    @abstractmethod
    def get_price(self):
        """
        Abstract method to get the price of the menu item.
        """
        pass

class FoodItem(MenuItem):
    """
    Concrete class for food items.
    """
    def __init__(self, name:str, price: float,is_veg:bool = False):
        super().__init__(name, price) # call the parent class constructor
        self.is_veg = is_veg

    def get_details(self):
        # Return the details of the food item as a string
        details = f"{self.name} - {self.price:.2f}" 
        if self.is_veg:
            details += " (veg)"
        return details
    
    def get_price(self):
        # Return the price of the food item
        return self.price
    
class DrinkItem(MenuItem):
    """
    Concrete class for drink items.
    """
    def __init__(self, name:str, price: float, is_cold:bool = False):
       super().__init__(name, price) # call the parent class constructor
       self.is_cold = is_cold

    def get_details(self):
        # Return the details of the drink item as a string
        details = f"{self.name} - {self.price:.2f}"
        details += " (cold)" if self.is_cold else " (hot)"
        return details

    def get_price(self):
        # Return the price of the drink item
        return self.price


# -----------------------------
# Abstraction for Payments
# -----------------------------
class Payment(ABC):
    """
    Abstract class for payment methods.
    """
    @abstractmethod
    def process_payment(self, amount: float)->str:  
        """
        Process the payment of a given amount.
        """
        pass


class CashPayment(Payment):
     """
    Concrete implementation for cash payments.
    """    
     def process_payment(self, amount: float)->str:
        return f"Cash payment of ${amount:.2f} received."
     

class CardPayment(Payment):
     """
    Concrete implementation for card payments.
    """    
     def process_payment(self, amount: float)->str:
        return f"Card payment of ${amount:.2f} processed successfully, payment received"
     

class MobilePayment(Payment):
     """
    Concrete implementation for mobile payments.
    """    
     def process_payment(self, amount: float)->str:
        return f"Mobile payment of ${amount:.2f} processed successfully, payment received"
     

# -----------------------------
# Encapsulation in Customer Class
# -----------------------------

class Customer:
    """
    Customer class encapsulating customer details.
    """
    def __init__(self, name: str, contact: str):
        self.__name = name # Encapsulated attribute with double underscore
        self.__contact = contact # Encapsulated attribute with double underscore private attribute

    
    def get_name(self):
        return self.__name
    
    def get_contact(self):
        return self.__contact
    

# -----------------------------
# Composition in Order Class
# -----------------------------

class Order:
    """
    Order class that aggregates menu items and processes payments.
    """

    def __init__(self, customer: Customer):
        self.customer = customer
        self.items = [] # List to store the menu items multible times
        self.total = 0.0 # Total price of the order  
        
    def add_item(self, item: MenuItem):
         """
        Adds a menu item to the order and updates the total.
        """
         self.items.append(item)
         self.total += item.get_price()
    
    def get_total(self):
        """
        Returns the total price of the order.
        """
        return self.__total
    
    def set_total(self, total: float):
        """
        Sets the total price of the order.
        """
        self.__total = total
    
    def generate_receipt(self):
        """
        Generates a receipt string with order details.
        """
        receipt = f"Receipt for {self.customer.get_name()}\n"
        receipt += "-" * 30 + "\n"
        for item in self.items:
                receipt += f"{item.get_details()}\n"
                receipt += "-" * 30 + "\n"
        receipt += f"Total: ${self.total:.2f}"
        return receipt
    
    def process_payment(self, payment_method: Payment):
        """
        Processes the order by printing the receipt and processing payment.
        Demonstrates polymorphism with the payment_method.
        """
        print(self.generate_receipt())  
        payment_status = payment_method.process_payment(self.total)
        print(payment_status)




# -----------------------------
# Main Application
# -----------------------------

if __name__ == "__main__":
    # Create a customer
    customer = Customer("John Doe", "1234567890")

    #create an order for the customer
    order = Order(customer)

    #Menu Items
    burger = FoodItem("Burger", 10.99)
    fries = FoodItem("Fries", 5.99)
    coke = DrinkItem("Coke", 2.99)
    coffee = DrinkItem("Coffee", 3.99)

   
   #add the items to the order
    order.add_item(burger)
    order.add_item(fries)
    order.add_item(coke)
    order.add_item(coffee)


 #payment methods
    customer_prefferd_payment = MobilePayment()

    #process the order
    order.process_payment(customer_prefferd_payment)
  