class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def print_account_details(self):
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")

a = Account(1238493, 1000, "jiw934")
a.print_account_details()