T = int(input())
while T:
    T -= 1
    J = set(input())
    S = input()
    c = 0
    for i in S:
        if i in J:
            c += 1

    print(c)
