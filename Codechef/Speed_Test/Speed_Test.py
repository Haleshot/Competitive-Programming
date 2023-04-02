T = int(input())
while T:
    T -= 1
    A, X, B, Y = map(int, input().split())
    if ((A//X) > (B // Y)):
        print("ALICE")