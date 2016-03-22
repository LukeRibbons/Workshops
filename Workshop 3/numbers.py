numbers_file = open("numbers.txt", "r")

first_number = int(numbers_file.readline())
second_number = int(numbers_file.readline())

print(first_number + second_number)

numbers_file.close()