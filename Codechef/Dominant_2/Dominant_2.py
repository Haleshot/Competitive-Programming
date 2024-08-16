from collections import Counter

T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    L = Counter(A)
    L1 = [i for i in L.values()]
    # print(L1)
    m = max(L1)
    if L1.count(m) == 1:
        print("YES")
    else:
        print("NO")
