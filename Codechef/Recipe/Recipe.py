import numpy as np
T = int(input())
while T:
    T -= 1
    N = list(map(int(input())))

    gcd = gcd_calc(N[1], N[2])
    for i in range(2, N):
        gcd=gcd_calc(gcd, N[i])