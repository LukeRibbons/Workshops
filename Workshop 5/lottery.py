import random
PICK_LENGTH = 6
MINIMUM = 1
MAXIMUM = 45
picks = int(input("How many quick picks? "))
for i in range(picks):
    pick_list = [0] * PICK_LENGTH
    for a in range(PICK_LENGTH):
        pick_list[a] = random.randint(MINIMUM, MAXIMUM)
        while pick_list.count(pick_list[a]) >= 2:
            pick_list[a] = random.randint(MINIMUM, MAXIMUM)
    pick_list = sorted(pick_list)
    for a in range(PICK_LENGTH):
        print("{:3}".format(pick_list[a]), end=" ")
    print()