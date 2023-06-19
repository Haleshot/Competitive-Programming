import numpy as np
T = int(input())
while T:
    T -= 1
    N = list(map(int, input().split()))
    B = []
    C = []
    for i in range(1, len(N)):
        B.append(N[i])
    gcd = B[0]
    for i in range(1, N[0] - 1):
        gcd = np.gcd(gcd, B[i])
    for i in range(N[0] - 1):
        C.append(B[i]//gcd)
    for i in range(N[0] - 1):
        print(C, end = ' ')