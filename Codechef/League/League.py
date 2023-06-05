T = int(input())
while T:
    T -= 1
    N = int(input())
    if N % 2 == 0:
        print(int((N/2) * 3))
    else:
        print(int(((N - 1)/2) * 3))