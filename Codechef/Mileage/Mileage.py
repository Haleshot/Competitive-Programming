T = int(input())
while T:
    T -= 1
    N, X, Y, A, B = map(int, input().split())
    petrol = (N / A) * X
    diesel = (N / B) * Y
    if petrol > diesel:
        print("DIESEL")
    elif petrol < diesel:
        print("PETROL")
    else:
        print("ANY")
