T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    FS = ''
    i = 0
    S = list(S)
    while i < N - 1:
        j = ''
        j += S[i]
        S[i] = S[i + 1]
        S[i + 1] = j
        i += 2
    for k in S:
        FS += chr(122 - ord(k) + 97)
    print(FS)
