N1, N2, N3 = list(map(int, input().split()))

# N1_vot, N2_vot, N3_vot = [], [], []

# for i in range(N1):
#     N1_vot.append(int(input()))

# for i in range(N2):
#     N2_vot.append(int(input()))

# for i in range(N3):
#     N3_vot.append(int(input()))

# final_l = []
# for i in range(N1):
#     c = N1_vot[i]
#     if c in N2_vot or c in N3_vot:
#         final_l.append(c)

# for i in range(N2):
#     c = N2_vot[i]
#     if c in N1_vot or c in N3_vot:
#         final_l.append(c)

# for i in range(N3):
#     c = N3_vot[i]
#     if c in N1_vot or c in N2_vot:
#         final_l.append(c)
# print(len(set(final_l)))
# final_l = list(set(final_l))
# final_l.sort()
# for i in final_l:
#     print(i)

N1_vot = set([int(input()) for _ in range(N1)])
N2_vot = set([int(input()) for _ in range(N2)])
N3_vot = set([int(input()) for _ in range(N3)])

result = (N1_vot & N2_vot) | (N2_vot & N3_vot) | (N1_vot & N3_vot)
result = list(result)
print(len(result))
result.sort()
[print(i) for i in result]