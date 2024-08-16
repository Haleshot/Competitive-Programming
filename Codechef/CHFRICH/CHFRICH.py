T = int(input())
while T:
    T -= 1
    A, B, X = map(int, input().split())
    c = 0
    while True:
        A += X
        c += 1
        if A == B:
            print(c)
            break
