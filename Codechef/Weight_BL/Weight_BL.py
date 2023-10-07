T = int(input())
while T:
    T -= 1 
    W1, W2, X1, X2, M = map(int, input().split())
    if(W2 >= W1 + (M * X1) and W2 <= W1 + (M * X2)):
        print(1)
    else:
        print(0)