T = int(input())
while T:
    T -= 1
    A = int(input())
    Z = ""
    H = str(input())
    for j in range(0, A, 2):
        if H[j] + H[j + 1] == "00":
            Z = Z + "A"
        elif H[j] + H[j + 1] == "01":
            Z = Z + "T"
        elif H[j] + H[j + 1] == "10":
            Z = Z + "C"
        else:
            Z = Z + "G"
    print(Z)
