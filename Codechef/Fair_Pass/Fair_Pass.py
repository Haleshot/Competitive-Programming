T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    req = N + 1
    if K >= req:
        print("YES")
    else:
        print("NO")