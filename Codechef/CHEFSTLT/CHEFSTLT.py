T = int(input())
while T:
    T -= 1
    S1 = input()
    S2 = input()
    q1 = S1.count("?")
    q2 = S2.count("?")
    print(len(S2) - max(q1, q2), " ", len(S1))