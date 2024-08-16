T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(str, input().split()))
    new_A = []
    for i in A:
        if i not in new_A:
            new_A.append(i)
    new_A = list(map(int, new_A))
    new_A.sort(reverse=True)
    print(new_A[0] + new_A[1])
