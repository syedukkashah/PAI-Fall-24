class Account:
    def __init__(self, accountNum, balance, security_code):
        self.__account_no = accountNum
        self.__account_bal = balance
        self.__security_code = security_code

    def display_info(self):
        print(f"Account No: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")


account = Account("123456", 1000.50, "abc123")
account.display_info()
