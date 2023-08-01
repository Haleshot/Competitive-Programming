T = int(input())
while T:
    T -= 1 
    N = int(input().split())
    S = input()
    l1 = [], l2 = []
    for k in range(0, N//2):
        l1.append(S[k])
    for j in range(N//2, N):
        l2.append(S[j])

    