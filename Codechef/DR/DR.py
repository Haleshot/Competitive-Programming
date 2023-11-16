T = int(input())
while T:
    T -= 1
    X = int(input())
    Y = list(map(int,input().split()))
    A = []
    B = []
    for j in range(0, len(Y)):
        if Y[j] == Y[j - 1]:
            A.append(Y[j])
        else:
            B.append(Y[j])
    
