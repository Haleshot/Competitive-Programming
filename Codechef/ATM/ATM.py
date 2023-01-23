T = int(input())

while T > 0:

    T -= 1
    N, K = map(int, input().split())
    l = list(map(int, input().split()))
    l_2 = []
    if len(l) == N:
        for i in l:
            if i <= K:
                K -= i
                l_2.append(1)
            else:
                l_2.append(0)
        for i in l_2:
            print(i, end = "")
        print()
