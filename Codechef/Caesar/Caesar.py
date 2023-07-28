Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    S = input()
    T = input()
    U = input()
    cipher = abs(ord(S[0]) - ord(T[0]))
    rotK_U = []
    for i in range(N):
        # rotK_U[i] = chr(ord(U[i]) + cipher)
        if (chr(ord(U[i]) + cipher)) > 122:
            pass
        else:
            print(chr(ord(U[i]) + cipher), end = "")
    print()
    # print(rotK_U)