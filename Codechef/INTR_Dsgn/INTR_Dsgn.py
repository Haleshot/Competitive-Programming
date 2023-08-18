T = int(input())
while T:
    T -= 1
    X1, Y1, X2, Y2 = map(int, input().split())
    print(min((X1 + Y1), (X2 + Y2)))