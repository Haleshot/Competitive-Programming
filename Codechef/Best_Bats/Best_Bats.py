import math
T = int(input())
while T:
    T -= 1
    L = list(map(int, input().split()))
    K = int(input())
    L.sort()
    g = L[11 - K]
    c1 = L.count(g)
    c = 0
    for i in range(11 - K, 11):
        if L[i] == g:
            c += 1
        else:
            break
    print(math.comb(c1, c))