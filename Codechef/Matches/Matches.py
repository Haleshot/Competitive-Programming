T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    d = {0 : 6, 1 : 2, 2 : 5, 3 : 5, 4 : 4, 5 : 5, 6 : 6, 7 : 3, 8 : 7, 9 : 6}
    total = A + B
    c = 0
    for i in str(total):
        c += d[int(i)]
    print(c)