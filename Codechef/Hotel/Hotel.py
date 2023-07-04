T = int(input())
while T:
    T -= 1
    N = int(input())
    arr = list(map(int, input().split()))
    dept = list(map(int, input().split()))
    arr.sort()
    dept.sort()
    current, maximum, i, j = 0, 0, 0, 0

    while i < N and j < N:
        if arr[i] < dept[j]:
            i += 1
            current += 1
        else:
            j += 1
            current -= 1
        if current > maximum:
            maximum = current
            
    print(maximum)