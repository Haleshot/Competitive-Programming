# T = int(input())
# while T:
#     T -= 1
#     N, K, S = map(int, input().split())
#     l = [i for i in range(2 * N + 1) if (i % 2 == 1)]
#     l2 = l.copy()
#     for i in range(N + K - 1):
#         temp = l2[i]
#         l2.extend([temp] * (K- 1))
#         if sum(l2) == S:
#             print(temp)
#             break
#         l2 = l.copy()

T = int(input())
while T:
    T -= 1
    N, K, S = map(int, input().split())
    c = 0
    for i in range(2 * N + 1):
        if (i % 2 == 1):
            c += i
    print(int((S - c)/(K - 1)))