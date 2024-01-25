T = int(input())
while T:
    T -= 1
    N = int(input())
    L = list(map(int, input().split()))
    G = list(map(int, input().split()))
    f, b = True, True
    for i in range(N):
        if L[i] > G[i]:
            f = False
        if L[i] > G[N - i - 1]:
            b = False
    if (f and b):
        print("both")
    elif (f):
        print("front")
    elif (b):
        print("back")
    else:
        print("none")