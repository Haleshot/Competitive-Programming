T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))
    s = A + D
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    c = 0
    for i in d:
        if d[i] > c:
            c = d[i]
    print(c)