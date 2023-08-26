import math
T = int(input())
while T:
    T -= 1
    L = list(map(int, input().split()))
    K = int(input())

    m = L[11 - K]
    c1 = L.count(m)
    c = 0
    for i in range(11 - K, 11):
        if L[i] == m:
            c += 1
    print(math.comb(c1,c))