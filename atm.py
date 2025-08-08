balance = 10000
amount = float(input("enter amount to withdraw: "))
if amount > balance:
   print("insufficient balance")
if amount <= balance and amount > 0:
    if amount % 1000 == 0:
       balance -= amount
       print("withdraw successful")
       print(balance)
    else:
        print("invalid amount")
else:
    print("out of range")
