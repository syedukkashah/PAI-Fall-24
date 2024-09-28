from os import access


class BankAccount:
    def __init__(self, acc_num, balance, date_oo, name):
        self.__acc_num = acc_num
        self.__balance = balance
        self.__data_of_opening = date_oo
        self.customer_name = name

    def deposit(self, amount):
        if(amount>0):
            self.__balance +=amount
        else:
            print("invalid input")

    def withdraw(self, amount):
        if(amount<self.__balance and amount>0):
            self.__balance -= amount
        else:
            print("invalid input")

    def check_balance(self):
        return self.__balance

acc = BankAccount(12, 1000, "9/16/2024", "ukkashah")
print(acc.check_balance())
acc.deposit(50)
print(acc.check_balance())
acc.deposit(-2)
acc.withdraw(100)
print(acc.check_balance())
acc.withdraw(9000)



