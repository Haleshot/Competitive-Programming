T = int(input())
while T:
    T -= 1
    A, B, C, D = map(int, input().split())
    if (A + C) == 180 or (B + D) == 180:
        print("YES")
    else:
        print("NO")
