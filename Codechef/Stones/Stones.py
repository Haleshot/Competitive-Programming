T = int(input())
while T:
    T -= 1
    J = set(input())
    S = input()
    c = 0
    for i in J:
        if i in S:
            c += 1

    print(c)