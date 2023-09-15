L = []
for i in range(31):
    for j in range(i + 1, 31):
        L.append(pow(2, i) + pow(2, j))
L.sort()

T = int(input())
while T:
    T -= 1
    N = int(input())
    i = 0 
    while(L[i] < N):
        i += 1 
    print(min(abs(L[i] - N), abs(N - L[i - 1])))