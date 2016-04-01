import random
picks = int(input("How many quick picks? "))
for i in range(picks):
    pick_list = [0] * 6
    for a in range(6):
        pick_list[a] = random.randint(1, 45)
        while pick_list.count(pick_list[a]) >= 2:
            pick_list[a] = random.randint(1, 45)
    pick_list = sorted(pick_list)
    print("{:3} {:3} {:3} {:3} {:3} {:3}".format(pick_list[0], pick_list[1], pick_list[2], pick_list[3], pick_list[4], pick_list[5]))