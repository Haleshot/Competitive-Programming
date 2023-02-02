T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))

    d = {}
    c = 0
    for i in range(len(A)):
        if A[i] in d.keys():
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    c = 0
    l = list(d.values())
    for i in l:
        if i > 2:
            c += 1
            break
    if c > 0:
        print("NO")
    
    else:
        print("YES")
