T = int(input())
X = list(map(int, input().split()))
c = X[:3]
while T:
    T -= 1
    S = min(c[-3:]) + X[i]
    c.append(S)
print(min(c[-3:]))