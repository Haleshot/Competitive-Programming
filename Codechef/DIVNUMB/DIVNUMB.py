T = int(input())
while T:
    T -= 1
    N, A, B, C = map(int, input().split())
    lst = set()
    for i in range(1, N + 1):
        lst.add(i * A)
        lst.add(i * B)
        lst.add(i * C)
    lst = sorted(lst)
    print(lst[N - 1])
