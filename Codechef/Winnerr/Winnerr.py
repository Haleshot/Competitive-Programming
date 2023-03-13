T = int(input())
while T:
    T -= 1
    Pa, Pb, Qa, Qb = map(int, input().split())
    max_P = max(Pa, Pb)
    max_Q = max(Qa, Qb)
    if (max_P > max_Q):
        print("Q")
    elif (max_P < max_Q):
        print("P")
    else:
        print("TIE")