T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    totalArea = 0
    for i in range(N):
        l = A[i]
        b = l[i + 1]
        if (A.count(l) == 2 and A.count(b) == 2):
            area = l * b
            if (area > totalArea):
                totalArea = area
    
    print(totalArea)