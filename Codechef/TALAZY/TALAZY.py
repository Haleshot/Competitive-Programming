# comp, time, s = 0, 0, 1
s = 0

def calculateTime(N, B, M):
    # global comp, time, s
    global s
    # print(comp, ", ", time)

    
    if N == 0:
        return s - B
    
    else:
        if N % 2 == 0:
            s += N // 2 * M
            s += B
            return calculateTime(N - N // 2, B, 2 * M)

        else:
            s += (N + 1) // 2 * M
            s += B
            return calculateTime(N - (N + 1) // 2, B, 2 * M)


T = int(input())
while T:
    T -= 1
    N, B, M = map(int, input().split())
    s = 0
    print(calculateTime(N, B, M))