# #custom exception handling

# class InsufficientFundsError(Exception): # inherit from Exception
#     def __init__(self, account_number, attempted_withdrawal, balance):
#         self.account_number = account_number
#         self.attempted_withdrawal = attempted_withdrawal
#         self.balance = balance
#         super().__init__(f"Insufficient funds in account {account_number}. "
#                          f"Attempted withdrawal: {attempted_withdrawal}, "
#                          f"Available balance: {balance}")

    
        



# def withdraw(account_number, amount, balance):
#     if amount > balance:
#         raise InsufficientFundsError(account_number, amount, balance)
#     return balance - amount


# try:
#     balance = withdraw("123456", 300, 500)
# except InsufficientFundsError as e:
#     print(e)
# else:
#     print("Withdrawal successful. New balance:", balance)
    