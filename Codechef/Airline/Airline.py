T = int(input())
while T:
    T -= 1
    l = []
    A, B, C, D, E = map(int, input().split())
    l = [A, B, C]
    l.sort()
    if l[0] <= E:
        sum = l[1] + l[2]
        if sum <= D:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")