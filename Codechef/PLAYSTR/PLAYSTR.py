T = int(input())
while T:
    T -= 1
    N = int(input())
    S = list(input())
    R = list(input())
    c = 0
    if S == R:
        print("NO")
    else:
        # one_count = list(S).count("1")
        # print(one_count)