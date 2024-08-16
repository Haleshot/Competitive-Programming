T = int(input())
while T:
    T -= 1
    A, B, C, X = map(int, input().split())
    if (A + B) >= X or (A + C) >= X or (B + C) >= X:
        print("YES")
    else:
        print("NO")
