exchanges_rates = {'PKR':305.0, 
                   'EUR': 0.85,
                   'INR': 83.0,
                   'JPY': 146.0,
                   'USD': 1.0
                   }
choice = input("Which Currency would you like to convert?(USD, EUR, PKR, INR, JPY)")   
convert = input("Which curreny would you like to convert this too?(USD, EUR, PKR, INR, JPY)")
amount = float(input("Enter amount you want to convert: "))
amount_USD = amount / exchanges_rates[choice] # we first convert amount to USD
converted = amount_USD*exchanges_rates[convert] # then we convert to desired currency
print(amount," ", choice, " is ", converted, " ", convert)


