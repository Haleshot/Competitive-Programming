T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    if (A + B) == C:
        print("YES")
    else:
        print("NO")
