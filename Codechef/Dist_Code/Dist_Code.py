T = int(input())
while T:
    T -= 1
    S = input()
    d = {}
    c = 0
    for i in range(len(S) - 1):
        x = S[i:i + 2]
        print(x)