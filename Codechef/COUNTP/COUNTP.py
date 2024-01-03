T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    F, C = 0, 0
    for i in A:
        if(i % 2 == 1):
            C += 1
    if(C % 2 == 1 or C == 0):
        print('NO')
    else:
        print('YES')