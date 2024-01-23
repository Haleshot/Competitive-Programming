import collections
T  = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    c = 0
    freq = collections.Counter(S)
    for i in freq.values():
        if i == 1:
            c += 1
    if c > 0:
        print("NO")
    else:
        print("YES")