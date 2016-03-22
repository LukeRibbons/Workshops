LOWER = 10
UPPER = 100

as_integer = int(input("Enter a number ({}-{}):".format(LOWER, UPPER)).strip())

while as_integer >= 10 and as_integer <= 100:
    print("{:<3} {}".format(as_integer, chr(as_integer)))
    as_integer = int(input("Enter a number ({}-{}):".format(LOWER, UPPER)))

print("You have input an invalid number, program end.")

for i in range(10, 120, 11):
    print("{:>3} {}".format(i, chr(i)))