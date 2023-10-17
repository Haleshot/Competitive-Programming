T = int(input())
while T:
    T -= 1
    R = 1
    n = int(input())
    nums = list(map(int, input().split()))
    k = []
    for i in range(len(nums)):
        k.append(nums[i])
    k.sort()
    for j in range(len(k)):
        if nums[j] != k[j]:
            R = 0
    if R == 1:
        print("YES")
    else:
        print("NO")