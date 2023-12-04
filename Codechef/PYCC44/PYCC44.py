N = int(input())
for i in range(N):
    S, X, Y, Z = [int(x) for x in input().split()]
    if(X + Y + Z <= S):
        print(0)
    elif(Z + min(X, Y) > S):
        print(2)
    else:
        print(1)