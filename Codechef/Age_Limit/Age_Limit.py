T = int(input())
while T:
    T -= 1
    X, Y, A = map(int, input().split())
    if (A >= X and A < Y):
        print("YES")
    else:
        print("NO")