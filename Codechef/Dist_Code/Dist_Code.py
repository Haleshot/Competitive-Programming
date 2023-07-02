T = int(input())
while T:
    T -= 1
    S = input()
    d = {}
    c = 0
    for i in range(len(S) - 1):
        x = S[i:i + 2]
        d[x] = 0
    for i in range(len(S) - 1):
        x = S[i:i + 2]
        if d[x] == 0:
            d[x] += 1
            c += 1

    print(c)
        