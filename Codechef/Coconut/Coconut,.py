T = int(input())
while T:
    T -= 1
    xa, xb, Xa, Xb = map(int, input().split())
    req_1 = Xa/xa
    req_2 = Xb/xb
    print(req_1 + req_2)