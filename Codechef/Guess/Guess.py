from math import gcd

T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    l = []
    alice_c = 0
    bob_c = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            l.extend([[i, j]])
    for i in l:
        if (i[0] + i[1]) % 2 == 1:
            alice_c += 1
        else:
            bob_c += 1
    common = gcd(alice_c, len(l))
    alice_c = alice_c // common
    print(alice_c)
    denom = len(l) // common
    print(alice_c, "/", denom, sep='')
    