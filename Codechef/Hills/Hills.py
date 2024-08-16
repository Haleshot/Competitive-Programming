T = int(input())
while T:
    T -= 1
    N, U, D = map(int, input().split())
    H = list(map(int, input().split()))
    c, c1 = 1, 0
    for i in range(N - 1):
        l1, l2 = H[i], H[i + 1]
        # print(l1, " ", l2)
        if ((l2 - l1) <= U) and ((l2 - l1) > 0):
            c += 1

        elif (l1 - l2) > D and c1 == 0:
            c1 += 1
            c += 1
            # print(c1)

        elif (((l1 - l2) <= D) and c1 <= 1) and ((l1 - l2) > 0):
            c += 1

        elif (l1 - l2) == 0:
            c += 1
        else:
            break

    print(c)
