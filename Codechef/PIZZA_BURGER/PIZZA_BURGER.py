T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if (Y <= Z and X >= Y):
        print("PIZZA")
    elif (X >= Z and Y > Z):
        print("BURGER")
    else:
        print("NOTHING")