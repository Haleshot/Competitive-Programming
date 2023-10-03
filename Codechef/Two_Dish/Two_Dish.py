T = int(input())
while T:
    T -= 1
    N, A, B, C = map(int, input().split())
    D = A + C 
    if N <= D and N <= B:
        print('YES')
    else:
        print('NO')