# Payment class polymorphism

class Payment:
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class CashPayment(Payment):
    def process_payment(self, amount):
        return f"Processing cash payment of ${amount}"
    
class DebitCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing debit card payment of ${amount}"
    
def process_order(payment_method, amount):
    return payment_method.process_payment(amount)


if __name__ == "__main__":
    payment_method = [
        CreditCardPayment(),
        CashPayment(),
        DebitCardPayment()
    ]
    

    for payment in payment_method:
        print(process_order(payment, 100))