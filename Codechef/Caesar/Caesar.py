Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    S = input()
    T = input()
    U = input()
    rotK_U = ""
    if (T[0] > S[0]):
        cipher = ord(T[0]) - ord(S[0])
        for i in range(N):
            if (ord(U[i]) + cipher) > 122:
                rotK_U += chr(((ord(U[i]) + cipher)) - 26)
            else:
                rotK_U += chr(((ord(U[i]) + cipher)))
    elif (T[0] < S[0]):
        cipher = ord(S[0]) - ord(T[0])
        for i in range(N):
            if (ord(U[i]) - cipher) < 97:
                rotK_U += chr(((ord(U[i]) - cipher)) + 26)
            else:
                rotK_U += chr(((ord(U[i]) - cipher)))
    
    else:
        print(U)
    print(rotK_U)
    # print(rotK_U)