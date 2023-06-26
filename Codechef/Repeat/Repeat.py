T = int(input())
while T:
    T -= 1
    N, K, S = map(int, input().split())
    length = N + K - 1
    l = []
    for i in range(2 * N + 1):
        if (i % 2 == 1):
            l.append(i)

    for i in range(length - N):
        temp = l[i]
        for j in range(K - l.count(temp)):
            l.append(temp)
        print(l)
        # if sum(l) == S:
        #     print(temp)
        #     break