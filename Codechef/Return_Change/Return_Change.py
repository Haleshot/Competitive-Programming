T = int(input())
while T:
    T -= 1
    X = int(input())
    nearest = round(X / 10) * 10
    if abs(X - nearest >= 5):
        nearest += 10
    print(100 - nearest)
