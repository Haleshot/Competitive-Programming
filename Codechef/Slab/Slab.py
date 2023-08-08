T = int(input())
while T:
    T -= 1
    N = int(input())
    if (N <= 250000):
        print(N)
    elif (N > 250000 and N <= 500000):
        net_total = N - 0.05 * N
        print(net_total)
