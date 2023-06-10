T = int(input())
while T:
    T -= 1
    N, X, Y = map(int, input().split())
    if ((X * Y) >= N):
        print("YES")
    else:
        print("NO")