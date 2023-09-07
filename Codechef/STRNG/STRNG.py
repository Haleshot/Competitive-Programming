def gcd(x, y):
    while(y):
        x, y= y, x % y
    return x

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    a = [arr[0]]
    b = [arr[n-1]]
    for i in range(1, n):
        a.append(gcd(a[-1], arr[i]))
        b.append(gcd(b[-1], arr[n-1-i]))
    ans = a[-1]
    for i in range(n):
        if(i > 0 and i < n - 1):
            if(gcd(a[i - 1], b[n - 2 - i]) != 1):
                count += 1
        if(i == 0):
            if(b[n - 2] != 1):
                count += 1
        if(i == n - 1):
            if(a[n - 2] != 1):
                count += 1
    if(ans == 1):
        print(count)
    else:
        print(n)