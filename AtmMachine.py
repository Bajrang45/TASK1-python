balance = 10000

amount = float(input("Enter Withdrawal Amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")