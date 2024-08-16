T = int(input())
while T:
    T -= 1
    P = int(input())
    if ((P % 100) + (P // 100)) <= 10:
        print((P % 100) + (P // 100))
    else:
        print(-1)
