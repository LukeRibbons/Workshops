name = input('Enter name:')

message_string = '''(H)ello
(G)oodbye
(Q)uit'''
print(message_string)

choice = input().capitalize()

while choice != 'Q':
    if choice == 'H':
        print('Hello', name)
    elif choice == 'G':
        print('Goodbye', name)
    else:
        print('Invalid')
    print(message_string)
    choice = input().capitalize()

print('Finished')
