import numpy as np
T = int(input())
while T:
    T -= 1
    N = list(map(int(input())))
    B = []
    C = []
    for i in range(N[0]):
        B.append(N[i])
    gcd = B[0]
    for i in range(N[0] - 1):
        C.append(B[j]//gcd)
    for i in range(N[0] - 1):
        print(C, end = ' ')