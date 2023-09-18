T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    
    res = [1 for i in range(N)]
    for i in range(N-2, -1, -1):
        if A[i + 1] * A[i] < 0:
            res[i] = res[i + 1] + 1 
    for i in res[:-1]:
        print(i, end = " ")
    print(res[-1])