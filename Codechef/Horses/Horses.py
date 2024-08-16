T = int(input())
while T:
    T -= 1
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    diff = 10
    minimum = []
    for i in range(1, N):
        minimum.append(S[i] - S[i - 1])

    print(min(minimum))
