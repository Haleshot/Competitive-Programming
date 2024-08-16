from collections import Counter

T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    D = Counter(A)
    print(N - max(D.values()))
