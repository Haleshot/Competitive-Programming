T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    if (N <= X):
        print("YES")
    else:
        print("NO")