T = int(input())
while T:
    T -= 1
    X, M = map(int, input().split())
    numNew = ""
    for i in str(X):
        d = int(i)
        numNew += str(d ** M % 10)
    revNum = numNew[::-1]
    if int(revNum) % 7 == 0:
        print("yes")
    else:
        print("no")