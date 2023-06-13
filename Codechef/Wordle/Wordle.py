T = int(input())
while T:
    T -= 1
    S = input()
    T = input()
    for i in range(5):
        if S[i] == T[i]:
            print("G", end = '')
        else:
            print("B", end = '')