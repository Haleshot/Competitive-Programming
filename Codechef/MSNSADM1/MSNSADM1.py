T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = [] * N
    for i in range(N):
        sum.append((20 * A[i]) - (10 * B[i]))
        if sum[i] < 0:
            sum[i] = 0
    print(max(sum))
