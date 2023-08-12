T = int(input())
while T:
    T -= 1
    N = int(input())
    L = list(map(int, input().split()))
    maximum = -1
    for i in range(N):
        for j in range(i + 1, N):
            diff = L[j] - L[i]
            # print(diff)
            if (diff > maximum):
                maximum = diff
                # print("YES")
    if maximum > 0:
        print(maximum)
    else:
        print("UNFIT")