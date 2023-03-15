T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    total = X * 3
    print(N//total)