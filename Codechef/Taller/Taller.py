T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if X > Y:
        print("A")
    else:
        print("B")
