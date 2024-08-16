T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    prod = X * Y
    print(prod // 100)
