T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    totalArea = 0
    flag = False
    for i in range(N - 1):
        l = A[i]
        b = A[i + 1]
        if (A.count(l) == 2 and A.count(b) == 2):
            flag = True
            area = l * b
            if (area > totalArea):
                totalArea = area
    if (flag):
        print(totalArea)
    else:
        print(-1)