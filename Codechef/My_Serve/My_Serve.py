T = int(input())
while T:
    T -= 1
    P, Q = map(int, input().split())
    points = P + Q
    if (points % 4 == 0 or points % 4 == 1):
        print("ALICE")
    else:
        print("BOB")