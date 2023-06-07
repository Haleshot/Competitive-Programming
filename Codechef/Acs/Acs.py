T = int(input())
while T:
    T -= 1
    P = int(input())
    if P % 100 == 0:
        print(P/100)
    elif P % 100 != 0:
        c = P % 100
        if len(str(c)) == 2:
            print(-1)
        else:
            print(int(c + 1))
    else:
        print(-1)