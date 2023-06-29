import math

X, N = map(int, input().split())
c = 0
while N:
    N -= 1
    H = input()
    i, j = 0, 54
    for _ in range(9):
        l = H[i:i+4] + H[j - 2:j]
        c += math.comb(l.count('0'), X)
        i += 4
        j -= 2
print(c)