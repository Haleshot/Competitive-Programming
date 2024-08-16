T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    c1, c2, c3 = 0, 0, 0
    for i in range(N):
        if S[i] == "Y":
            c1 += 1
        elif S[i] == "N":
            c2 += 1
        elif S[i] == "I":
            c3 += 1
    if c2 == N:
        print("NOT SURE")
    elif c1 > 0:
        print("NOT INDIAN")
    elif c3 > 0:
        print("INDIAN")
