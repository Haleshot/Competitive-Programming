T = int(input())
for i in range(T):
    X = int(input())
    Y = list(map(int,input().split()))
    A = []
    B = []
    for j in range(0, len(Y)):
        if Y[j] == Y[j - 1]:
            A.append(Y[j])
        else:
            B.append(Y[j])
    
    for k in A:
        if k in B:
            B.remove(k)
    C = str(B)[1 : -1]
    D = C.replace(',', '')
    print(D)