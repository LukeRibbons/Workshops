try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:  # when the value is not an integer, so any letter, symbol or non whole number.
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # when the denominator is zero avoided by not entering 0 or a loop that checks for zero
    print("Cannot divide by zero!")
print("Finished.")
