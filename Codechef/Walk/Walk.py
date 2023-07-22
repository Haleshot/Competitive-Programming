T = int(input())
while T:
    T -= 1
    N = int(input())
    W = list(map(int, input().split()))
    max_number = max(W)
    temp = 0

    for i in W:
        if max_number >= i:
            max_number -= 1
        else:
            max_number = max(W) + 1
            temp = max_number
    if temp == 0:
        print(max(W))
    else:
        print(max(W) + 1)