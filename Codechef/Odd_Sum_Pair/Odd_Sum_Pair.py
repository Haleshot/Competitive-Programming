T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    if (((A + B) % 2 == 1) and ((A + C) % 2 == 1) and ((B + C) % 2 == 1)):
        print("YES")
    else:
        print("NO")
