T = int(input())
while T:
    T -= 1
    DDSA, DTOC, DDM = map(int, input().split())
    SDSA, STOC, SDM = map(int, input().split())
    D_tot = DDSA + DTOC + DDM
    S_tot = SDSA + STOC + SDM
    if D_tot > S_tot:
        print("Dragon")
    elif S_tot > D_tot:
        print("Sloth")
    elif D_tot == S_tot and DDSA > SDSA:
        print("Dragon")
    elif D_tot == S_tot and SDSA > DDSA:
        print("Sloth")
    elif D_tot == S_tot and DTOC > STOC:
        print("Dragon")
    elif D_tot == S_tot and STOC > DTOC:
        print("Sloth")
    elif D_tot == S_tot and SDSA == DDSA:
        print("TIE")
