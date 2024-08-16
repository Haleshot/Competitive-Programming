T = int(input())
while T:
    T -= 1
    N = int(input())
    L = list(map(int, input().split()))
    # maximum = -1
    # # matrix = [[maximum for j in range(i + 1, N)] for i in range(N - 1) if L[i + 1] - L[i] > maximum]
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         diff = L[j] - L[i]
    #         # print(diff)
    #         if (diff > maximum):
    #             maximum = diff
    #             # print("YES")
    # if maximum > 0:
    #     print(maximum)
    # else:
    #     print("UNFIT")

    minimum = L[0]
    maximum = 0
    for i in range(N):
        if L[i] < minimum:
            minimum = L[i]
        elif L[i] - minimum > maximum:
            maximum = L[i] - minimum
    if maximum > 0:
        print(maximum)
    else:
        print("UNFIT")
