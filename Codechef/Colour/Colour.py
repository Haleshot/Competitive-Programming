T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if (X == 1 and Y == 1 and Z == 1):
        print(3)
    
    elif (X == 0 and Y == 0 and Z == 0):
        print(0)