T = int(input())
while T:
    T -= 1 
    N = int(input())
    X = list(map(int, input().split()))
    final_worst, final_best = 1, 1
    c = 1
    new_X = []
    for i in range(N - 1):
        if X[i + 1] - X[i] <= 2:
            c += 1
        else:
            new_X.append(c)
            c = 1
    new_X.append(c)
    print(min(new_X), max(new_X))