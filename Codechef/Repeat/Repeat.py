T = int(input())
while T:
    T -= 1
    N, K, S = map(int, input().split())
    length = N + K - 1
    l = []
    for i in range(2 * N + 1):
        if (i % 2 == 1):
            l.append(i)
    l2 = l.copy()
    print(l2)
    for i in range(length):
        l2.reverse()
        temp = l2[i]
        for j in range(K - 1):
            l2.append(temp)
        print(l2)
        if sum(l2) == S:
            print(temp)
            break
        else:
            l2 = l.copy()