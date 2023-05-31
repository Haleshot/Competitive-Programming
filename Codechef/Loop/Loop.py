T = int(input())
while T:
    T -= 1
    A, B, M = map(int, input().split())
    t1 = abs(A - B)
    t2 = abs(M - t1)
    print(min(t1, t2))