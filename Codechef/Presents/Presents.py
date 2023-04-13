T = int(input())
while T:
    T-= 1
    N = int(input())
    if N % 5 == 0:
        temp = N / 5
        print(4 * temp)
    elif (N < 5):
        print(N)
    else:
        temp = N // 5
        print(N - temp)