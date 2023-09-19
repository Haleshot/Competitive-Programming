T = int(input())
while T: 
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    count, ans = 1, 0
    last = A[0]
    for i in A[1:]:
        if i >= last:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 1
        last = i
    ans += count*(count + 1) // 2
    print(ans)