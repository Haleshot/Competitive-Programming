T = int(input())
while T:
    T -= 1
    a, b, c, d, K = map(int, input().split())
    steps = abs(c - a) + abs(d - b)
    if steps == K:
        print("Yes")
    elif K > steps and (K - steps) %2 == 0:
        print("Yes")
    else:
        print("No")