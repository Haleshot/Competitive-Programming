N1, N2, N3 = list(map(int, input().split()))
N1_vot, N2_vot, N3_vot = [], [], []

for i in range(N1):
    N1_vot.append(int(input()))

for i in range(N2):
    N2_vot.append(int(input()))

for i in range(N3):
    N3_vot.append(int(input()))

final_l = []
for i in range(N1):
    c = N1_vot[i]
    if c in N2_vot or c in N3_vot:
        final_l.append(c)

for i in range(N2):
    c = N2_vot[i]
    if c in N1_vot or c in N3_vot:
        final_l.append(c)

for i in range(N3):
    c = N3_vot[i]
    if c in N1_vot or c in N2_vot:
        final_l.append(c)
print(len(set(final_l)))
for i in set(final_l):
    print(i)