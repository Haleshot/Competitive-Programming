T = int(input())
while T:
    T -= 1
    N = int(input())
    if (N <= 250000):
        print(N)
    elif (N > 250000 and N <= 500000):
        net_total = N - 0.05 * N
        print(net_total)
    
    elif (N > 500000 and N <= 750000):
        net_total = int(N - ((250000 * 0.05) + (N - 500000) * 0.1))
        print(net_total)
    
    elif (N > 750000 and N <= 1000000):
        net_total = int(N - ((250000 * 0.05) + (500000 * 0.1) + (N - 750000) * 0.15))
        print(net_total)

    elif (N > 1000000 and N <= 1250000):
        net_total = int(N - ((250000 * 0.05) + (500000 * 0.1) + (750000 * 0.15) + (N - 1000000) * 0.2))
        print(net_total)

    elif (N > 1250000 and N <= 1500000):
        net_total = int(N - ((250000 * 0.05) + (500000 * 0.1) + (750000 * 0.15) + (1000000* 0.2) + (N - 1250000) * 0.25))
        print(net_total)
    
    elif (N > 1500000):
        net_total = int(N - ((250000 * 0.05) + (500000 * 0.1) + (750000 * 0.15) + (1000000* 0.2) + (1250000* 0.25) + (N - 1500000) * 0.3))
        print(net_total)