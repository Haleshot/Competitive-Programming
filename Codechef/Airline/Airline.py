T = int(input())
while T:
    T -= 1
    l = []
    A, B, C, D, E = map(int, input().split())
    if (A + B) <= D and C <= E:
        print("YES")

    elif (A + C) <= D and B <= E:
        print("YES")

    elif (B + C) <= D and A <= E:
        print("YES")

    else:
        print("NO")
