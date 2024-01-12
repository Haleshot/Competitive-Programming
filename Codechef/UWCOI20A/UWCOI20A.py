T = int(input())
while T:
    T -= 1
    N = int(input())
    H = []
    for i in range(N):
        H.append(int(input()))
    print(max(H))