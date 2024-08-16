from collections import Counter

for _ in range(int(input())):
    N = int(input())
    A = Counter(input().split()).most_common(2)
    if len(A) == 2:
        print(A[0][0] if A[0][1] > A[1][1] else "CONFUSED")
    else:
        print(A[0][0])
