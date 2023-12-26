T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    if(N % 2 == 0 or X % 2 != 0):
        print('YES')
    else:
        print('NO')