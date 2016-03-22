x = int(input('Please enter x:'))
y = int(input('Please enter y:'))

print('Show the (E)ven numbers from x to y')
print('Show the (O)dd numbers from x to y')
print('Show the (S)quares of the numbers from x to y')
print('Do you want to (Q)uit the program?')

choice = input()
choice = choice.capitalize()

while choice != 'Q':
    if choice == 'E':
        if x % 2 == 1:
            for i in range(x + 1, y, 2):
                print(i, end=' ')
            print()
        else:
            for i in range(x, y, 2):
                print(i, end=' ')
            print()
    elif choice == 'O':
        if x % 2 == 0:
            for i in range(x + 1, y, 2):
                print(i, end=' ')
            print()
        else:
            for i in range(x, y, 2):
                print(i, end=' ')
            print()
    elif choice == 'S':
        for i in range(x, y):
            print(i ** 2, end=' ')
        print()
    print('Show the (E)ven numbers from x to y')
    print('Show the (O)dd numbers from x to y')
    print('Show the (S)quares of the numbers from x to y')
    print('Do you want to (Q)uit the program?')
    choice = input()
    choice = choice.capitalize()
print('Program exited')
