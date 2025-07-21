amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert coin: "))
    if coin in [25, 10, 5]:
        amount_due -= coin
    else:
        print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")
        continue
change_owed = -amount_due
print("Change Owed:", change_owed)
