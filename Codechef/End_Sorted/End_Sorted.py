T = int(input())
while T:
    T -= 1
    N = int(input())
    P = list(map(int, input().split()))
    c = 0
    index_1 = P.index(1)
    index_n = P.index(N)
    if index_1 < index_n:
        print(index_1 + N - 1 - index_n)
    else:
        print(index_1 + N - 2 - index_n)