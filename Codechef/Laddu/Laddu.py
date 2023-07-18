T = int(input())
while T:
    T -= 1
    activities = list(list(map(str, input().split())))
    contest_won = list(map(str, input().split()))
    top_contrib = input()
    bug_found = list(map(str, input().split()))
    contest_host = input()
    points = 0
    if (int(contest_won[1]) <= 20):
        points += 300 + (20 - int(contest_won[1]))
        if (top_contrib and bug_found and contest_host):
            points += 300 + int(bug_found[1]) + 50

    if (activities[1] == "INDIAN"):
        print(points//200)
    else:
        print(points//400)