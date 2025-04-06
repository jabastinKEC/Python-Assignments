def splitBill(totalBill, friends):
    if totalBill > 200:
        totalBill -= totalBill * 0.10
    splittedAmt = totalBill / friends
    return splittedAmt


totalBill = float(input("Enter the total bill amount: $"))
friends = int(input("Enter the number of friends: "))

splittedAmt = splitBill(totalBill, friends)

print(f"Each friend should pay: ${splittedAmt:.2f}")
