T = int(input())
while T:
    T -= 1
    X, P, Q = map(int, input().split())
    print((P - Q) * X)
