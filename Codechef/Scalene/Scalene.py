T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    scalene = [i for i in [A, B, C] if [A, B, C].count(i) == 1]
    if len(scalene) == 3:
        print("YES")
    else:
        print("NO")