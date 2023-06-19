import numpy as np
T = int(input())
while T:
    T -= 1
    N = list(map(int, input().split()))
    B = []
    C = []
    for i in range(1, len(N)):
        B.append(N[i])
    g = B[0]
    for i in range(1, len(B)):
        g = np.gcd(g, B[i])
    for i in range(len(B)):
        C.append(B[i]//g)
    for i in range(len(C)):
        print(C[i], end = ' ')
    print()