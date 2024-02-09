T=  int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    c = 0
    for i in range(N):
        if S[i : i + 2] == "10":
            c += 1
    print(c)
