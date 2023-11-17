T = int(input())
while T:
    A, B = map(int, input().split())
    Li = list(map(int, input().split()))
    res = []
    for i in range(0, A, B):
        temp =Li[i : i + B]
        res += temp[::-1]
    print(*res)