T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    print(min((3 * X), (2 * Y)))