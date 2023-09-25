T = int(input())
X = list(map(int, input().split()))
while T:
    T -= 1
    c = X[:3]
    for i in range(3, T):
        S = min(c[-3:]) + X[i]
        c.append(S)
    print(min(c[-3:]))