T  = int(input())
while T:
    T -= 1
    N = int(input())
    K = list(map(int, input().split()))
    P = int(input())
    temp = K[P - 1]
    K.sort()
    print(K.index(temp) + 1)