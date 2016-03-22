name_file = open("name.txt", "w")

name = input ("Please enter your name: ")
print(name, file=name_file)

name_file.close()

name_file = open("name.txt", "r")

name = name_file.read()
print("Your name is", name)

name_file.close()

