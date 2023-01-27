T = int(input())
while T:
    T -= 1
    l = []
    A, B, C, D, E = map(int, input().split())
    l = [A, B, C]
    sorted = l.sort()
    if sorted[0] <= E:
        sum = sorted[1] + sorted[2]
        if sum <= D:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")