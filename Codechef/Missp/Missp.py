T = int(input())
while T:
    T -= 1
    N = int(input())
    c = 0
    for i in range(N):
        ele = int(input())
        if ele % 2 == 1:
            c += 1

    print(c)