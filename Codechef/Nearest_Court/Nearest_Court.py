T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    middle = (X + Y) // 2
    print(max(abs(middle - X), abs(middle - Y)))
