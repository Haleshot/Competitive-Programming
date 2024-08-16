from collections import Counter

T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    for A, B in C.most_common(1):
        M = B
    print(N - M)
