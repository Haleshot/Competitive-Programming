T = int(input())
while T:
    T -= 1
    X, N = map(int, input().split())
    X /= 10
    score = int(N * X)
    print(score)
