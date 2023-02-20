T = int(input())
while T:
    T -= 1
    R1, R2, R3 = map(int, input().split())
    if (R1 > (R2 + R3)):
        print("YES")
    elif (R2 > (R1 + R3)):
        print("YES")
    elif (R3 > (R1 + R2)):
        print("YES")
    else:
        print("NO")