T = int(input())
while T:
    T -= 1
    N = int(input())
    V = [[0 for i in range(49)] for j in range(49)]
    maximum_list = [0] * 49
    for i in range(1, N + 1):
        S, E, C = list(map(int, input().split()))
    for end in range(49):
        for begin in range(end):
            maximum_list[end] = max(maximum_list[end], V[begin][end] + maximum_list[begin])
    print(maximum_list[48])