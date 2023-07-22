T = int(input())
while T:
    T -= 1
    N = int(input())
    W = list(map(int, input().split()))
    max_number = max(W)
    for i in W:
        if max_number >= i:
            print(max_number)
            max_number -= 1
        max_number = max(W) + 1
    print(max_number)