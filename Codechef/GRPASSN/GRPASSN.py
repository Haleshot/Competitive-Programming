T = int(input())
while T:
    T -= 1
    N = int(input())
    P = list(map(int, input().split()))
    groups = set(P)
    for g in groups:
        if P.count(g) % g != 0:
            print("NO")
            break
    else:
        print("YES")
