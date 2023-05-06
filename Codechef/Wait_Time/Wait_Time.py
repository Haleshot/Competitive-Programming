T = int(input())
while T:
    T -= 1
    K, X = map(int, input().split())
    print((7 * K) - X)