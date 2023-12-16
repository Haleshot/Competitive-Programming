T = int(input())
while T:
    T -= 1
    N, X, P = map(int, input().split())
    total = X * 3 + (N - X) * (-1)
    if (total >= P):
        print("PASS")
    else:
        print("FAIL")