T = int(input())
while T:
    T -= 1
    X, H = map(int, input().split())
    if X >= H:
        print("YES")
    else:
        print("NO")