T = int(input())
while T:
    T -= 1
    N, A = map(int, input().split())
    uninfected = N - A
    print(min(A, uninfected))