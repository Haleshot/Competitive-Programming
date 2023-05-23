T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    N -= 0.1*N
    least = min(M, N)
    if least == N:
        print("ONLINE")
    elif least == M:
        print("DINING")
    if M == N:
        print("EITHER") 