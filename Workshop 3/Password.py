MINIMUM = 5
MAXIMUM = 15
UPPERCASE = 1
LOWERCASE = 1
SPECIAL = 1
NUMBER = 1


def message():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters and contain".format(MINIMUM, MAXIMUM))
    print("      {} or more uppercase characters".format(UPPERCASE))
    print("      {} or more lowercase characters".format(LOWERCASE))
    print("      {} or more numbers".format(NUMBER))
    print("      and {} or more special characters:   !@#$%^&*()_-=+`~,./o'[]\<>?O{}|".format(SPECIAL, "{}"))


def n_lower_chars(string):
    return sum(1 for c in string if c.islower())


def n_upper_chars(string):
    return sum(1 for c in string if c.isupper())


def n_numbers(string):
    return sum(1 for c in string if c.isalnum())


def n_special_chars(string):
    return sum(1 for c in string if not c.isalnum() and not c.isspace())

message()
valid = False
password = input()

while not valid:
    if MAXIMUM >= len(password) >= MINIMUM \
            and n_upper_chars(password) >= UPPERCASE \
            and n_lower_chars(password) >= LOWERCASE \
            and n_numbers(password) >= NUMBER \
            and n_special_chars(password) >= SPECIAL:
                print("Your {} character password is valid: {}!".format(len(password), password))
                valid = True
    if not valid:
        print("Invalid password!")
        password = input()
