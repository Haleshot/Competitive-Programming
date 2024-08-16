def prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


for _ in range(int(input())):
    N1, N2 = list(map(int, input().split()))
    for i in range(N1, N2 + 1):
        if prime(i):
            print(i)
