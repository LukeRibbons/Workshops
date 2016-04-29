from guitar import Guitar

print("My guitars")
name = " "
guitars = []
while name != "":
    name = input("Name: ")
    if name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
if guitars:
    print("These are my guitars")
    for x in range(len(guitars)):
        if guitars[x].is_vintage():
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} (vintage)".format(x + 1, guitars[x].name,
                                                                   guitars[x].year, guitars[x].cost))
        else:
             print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(x + 1, guitars[x].name,
                                                                   guitars[x].year, guitars[x].cost))