T = int(input())
while T:
    T -= 1
    a = int(input())
    v = list(map(int, input().split()))
    even = []
    odd = []
    for i in v:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    ans = even + odd
    print(*ans)