from math import sqrt

T = int(input())
while T:
    T -= 1
    B, LS = map(int, input().split())
    print(round(sqrt(LS**2 - B**2), 4), round(sqrt(LS**2 + B**2), 4))
