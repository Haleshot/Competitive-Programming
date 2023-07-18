T = int(input())
while T:
    T -= 1
    activities = list(map(str, input().split()))
    contest_won = list(map(str, input().split()))
    top_contrib = input()
    bug_found = list(map(str, input().split()))
    contest_host = input()
    points = 0
    for i in range(int(activities[0])):
        if ("WON" in contest_won[0]):
            if (int(contest_won[1]) <= 20):
                points += 300 + (20 - int(contest_won[1]))
            else:
                points += 300
        
        if ("TOP" in top_contrib):
            points += 300

        if "BUG" in bug_found[0]:
            if (int(bug_found[1]) >= 50 and int(bug_found[1]) <= 1000):
                points += int(bug_found[1])

        if "HOSTED" in contest_host:
            points += 50


    if (activities[1] == "INDIAN"):
        print(points)
        print(points//200)
    else:
        print(points//400)