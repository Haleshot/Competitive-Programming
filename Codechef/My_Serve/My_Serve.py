T = int(input())
while T:
    T -= 1
    P, Q = map(int, input().split())
    points = P + Q - 1
    if (points % 2 == 0):
        print("BOB")
    else:
        print("ALICE")