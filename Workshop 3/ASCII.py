LOWER = 10
UPPER = 100

as_integer = int(input("Enter a number ({}-{}):".format(LOWER, UPPER)).strip())

while 10 <= as_integer <= 100:
    print("{:<3} {}".format(as_integer, chr(as_integer)))
    as_integer = int(input("Enter a number ({}-{}):".format(LOWER, UPPER)))

print("You have input an invalid number, program end.")

for i in range(10, 120, 11):
    print("{:>3} {}".format(i, chr(i)))


def get_number(lower, upper):
    if lower >= upper:
        return lower
    else:
        entered_number = input("Enter a number ({}-{}):".format(lower, upper))
        while not entered_number.isdecimal()or lower >= int(entered_number) >= upper:
            print("Please enter a valid number")
            entered_number = input("Enter a number ({}-{}):".format(lower, upper))
        return entered_number
number_entered = int(get_number(LOWER, UPPER))

print("{:<3} {}".format(number_entered, chr(number_entered)))
