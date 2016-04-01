months = int(input("How many months? "))
monthly_income = []
for i in range(months):
    monthly_income.append(float(input("Enter income for month {} ".format(i + 1))))

print("Income Report \n -------------")
total = float(0)
for i in range(months):
    total += monthly_income[i]
    print("Month {:2d} - Income: $ {:8.2f} Total: $ {:8.2f}".format(i + 1, monthly_income[i], total))