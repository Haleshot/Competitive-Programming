T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    print((Z - Y) // X)
