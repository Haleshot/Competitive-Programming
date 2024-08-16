T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    A1 = set(map(int, input().split()))
    for i in range(B):
        b1 = int(input())
        if b1 in A1:
            print("Found")
        else:
            print("Not Found")
