T = int(input())
while T:
    T -= 1
    N = int(input())
    P = list(map(int, input().split()))
    if (P[0] == 1 and P[N - 1] == N):
        print(0)
    else:
        pass