T  = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    server = 0
    alice = 0
    bob = 0
    for j in range(N):
        if((server == 0) and (S[j] == 'A')):
            alice += 1
        elif((server == 0) and (S[j] == 'B')):
            server = 1
        elif((server == 1) and (S[j] == 'B')):
            bob += 1
        else:
            server = 0
    print(alice, "", bob)