T = int(input())
while T:
    T -= 1
    activities = list(map(str, input().split()))
    points = 0
    for i in range(int(activities[0])):
        all_inputs= list(input().split())
        
        if ("WON" in all_inputs[0]):
            if (int(all_inputs[1]) <= 20):
                points += 300 + (20 - int(all_inputs[1]))
            else:
                points += 300
        
        if ("TOP" in all_inputs[0]):
            points += 300

        if "BUG" in all_inputs[0]:
            if (int(all_inputs[1]) >= 50 and int(all_inputs[1]) <= 1000):
                points += int(all_inputs[1])

        if "HOSTED" in all_inputs[0]:
            points += 50

    if (activities[1] == "INDIAN"):
        print(points)
        print(points//200)
    else:
        print(points//400)