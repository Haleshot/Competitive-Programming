T = int(input())
while T:
    T -= 1
    N = int(input())
    W = list(map(int, input().split()))
    print(max([W[i] + i for i in range(N)]))
