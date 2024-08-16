T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in A:
        if i >= 10 and i <= 60:
            count += 1
    print(count)
