from math import gcd

T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    # l = []
    # alice_c = 0
    # for i in range(1, N + 1):
    #     for j in range(1, M + 1):
    #         l.extend([[i, j]])
    # for i in l:
    #     if (i[0] + i[1]) % 2 == 1:
    #         alice_c += 1
    # common = gcd(alice_c, len(l))
    # alice_c = alice_c // common
    # denom = len(l) // common
    l = N * M
    if l % 2 == 0:
        print("1/2")
    else:
        print(str(l // 2), "/", str(l), sep='')
