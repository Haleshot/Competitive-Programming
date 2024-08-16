T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()

    if len(S) == N:
        d = {}
        count = 0

        for i in S:
            if i in d.keys():
                d[i] += 1

            else:
                d[i] = 1

        for i in d.values():
            if i % 2 == 0:
                count += 1
            else:
                count = 0
                break

        if count > 0:
            print("YES")
        else:
            print("NO")
