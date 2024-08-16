T = int(input())
while T:
    T -= 1
    U, V, A, S = map(int, input().split())
    measure_v = (U**2) - (2 * A * S)
    if measure_v > (V**2):
        print("No")
    else:
        print("Yes")
