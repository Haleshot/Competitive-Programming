T = int(input())
while T:
    T -= 1
    N, M, K = map(int, input().split())
    if M * K >= N:
        print("YES")
    else:
        print("NO")
