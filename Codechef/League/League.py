T = int(input())
while T:
    T -= 1
    N = int(input())
    if N % 2 == 0:
        print((N/2) * 3)
    else:
        print((N - 1/2) * 3)