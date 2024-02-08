T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    for i in D:
        if int(i) % K == 0:
            print(1, end='')
        else:
            print(0, end='')
    print()