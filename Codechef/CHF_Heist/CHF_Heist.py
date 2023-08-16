T = int(input())
while T:
    T -= 1
    D, d, P, Q = map(int, input().split())
    money = 0
    for i in range(d):
        money += P
    for j in range(i, D, d):
        money += (P + (j * Q))
    print(money)