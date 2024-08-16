from math import ceil


def eat_complete(bananas, k, h):
    elapsed = 0
    for pile in bananas:
        elapsed += ceil(pile / k)
        if elapsed > h:
            return False
    return True


T = int(input())
while T:
    T -= 1
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    i = 1
    j = max(A)
    min_k = j
    while i <= j:
        m = (i + j) // 2
        if eat_complete(A, m, H):
            if m < min_k:
                min_k = m
                j = m - 1
            else:
                break
        else:
            i = m + 1
    print(min_k)
