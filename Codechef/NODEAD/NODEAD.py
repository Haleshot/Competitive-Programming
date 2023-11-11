N, Q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(Q):
    arr2 = list(map(int, input().split()))
    if len(arr2) == 2:
        arr.pop(arr2[1] - 1)
    else:
        arr.insert(arr2[1] - 1, arr2[2])
    print(*arr)