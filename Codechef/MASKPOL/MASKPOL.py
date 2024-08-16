T = int(input())
while T:
    T -= 1
    N, A = map(int, input().split())
    uninf = N - A
    print(min(A, uninf))
