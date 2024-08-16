T = int(input())
while T:
    T -= 1
    N = int(input())
    cont_subs = N * (N + 1) / 2
    if cont_subs % 2 == 0:
        print(N)
    else:
        print(N - 1)
