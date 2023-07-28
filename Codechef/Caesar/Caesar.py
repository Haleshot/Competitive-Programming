import numpy as np
alp = np.arange(chr(0), chr(123))

Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    S = input()
    T = input()
    U = input()
    cipher = abs(ord(S[0]) - ord(T[0]))
    rotK_U = ""
    if (S[0] > N[0]):
        for i in range(N):
            # rotK_U[i] = chr(ord(U[i]) + cipher)
            if (ord(U[i]) + cipher) > 122:
                rotK_U += chr((ord(U[i]) + cipher)) - 26
            else:
                rotK_U += chr((ord(U[i]) + cipher))
    elif (S[0] > N[0]):
        for i in range(N):
            # rotK_U[i] = chr(ord(U[i]) + cipher)
            if (ord(U[i]) + cipher) > 122:
                rotK_U += chr((ord(U[i]) - cipher)) + 26
            else:
                rotK_U += chr((ord(U[i]) - cipher))
    
    else:
        print(U)
    print()
    # print(rotK_U)