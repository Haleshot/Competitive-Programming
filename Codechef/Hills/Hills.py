T = int(input())
while T:
    T -= 1
    N, U, D = map(int, input().split())
    H = list(map(int, input().split()))
    c, c1 = 0, 0
    for i in range(N - 1):
        l1, l2 = H[i], H[i + 1]
        if ((l1 - l2 <= abs(U)) or (((l1 - l2) <= D) and c1 <= 1)):
            c += 1
        if (l1 - l2) > D and c1 != 1:
            c1 += 1
            c += 1
        
    print(c)