T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    minimum = min(A, B, C)
    total = (A + B + C) - minimum
    print(total)