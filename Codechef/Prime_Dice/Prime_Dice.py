def isPrime(X):
    c = 1
    for i in range(2, X + 1):
        if X % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False


T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    total = A + B
    if isPrime(total):
        print("ALICE")
    else:
        print("BOB")
