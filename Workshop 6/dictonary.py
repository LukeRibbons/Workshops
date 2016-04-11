dictionary_data = open("dictionary.csv", "r")
list_of_colours = dictionary_data.read().strip().split('\n')
dictionary_of_colours = {}
for i in range(len(list_of_colours)):
    list_of_colours[i] = list_of_colours[i].split(",")
    dictionary_of_colours[list_of_colours[i][0].upper()] = list_of_colours[i][1]  # capitalized keys for ease of check
dictionary_data.close()

colour = input("Enter hexadecimal colour name: ").upper()
while colour != "":
    if colour in dictionary_of_colours:
        print(colour, "is", dictionary_of_colours[colour])
    else:
        print("Invalid short state")
    colour = input("Enter hexadecimal colour name: ").upper()