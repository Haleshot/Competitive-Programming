T = int(input())
while T:
    T -= 1
    N, X, Y, A, B = map(int, input().split())
    petrol = (X * A) * N
    diesel = (Y * B) * N
    if petrol > diesel:
        print("DIESEL")
    elif petrol < diesel:
        print("PETROL")
    else:
        print("ANY")