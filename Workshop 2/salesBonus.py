sales = float(input("Enter sales: $ "))
while sales > 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, sep="")
    sales = float(input("Enter sales: $ "))
print('You have not made any sales or lost money, you suck at this job')
