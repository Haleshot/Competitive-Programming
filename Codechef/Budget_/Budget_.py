T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    expense = Y * 30
    if expense <= X:
        print("YES")
    else:
        print("NO")