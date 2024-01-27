from collections import Counter
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    freq = Counter(A)
    most_rec_value = max(freq.values())
    end = []
    for values in freq.values():
        end.append(values)
    end.sort(reverse=True)
    # if end[0] == end[1] and end[0] == most_rec_value:
    #     print("CONFUSED")
    # else:
    #     # temp1 = freq.keys()
    #     # temp2 = freq.values()
    #     # temp = list(temp2).index(most_rec_value)
    #     # print(temp1[temp])
    #     value = [i for i in freq if freq[i] == most_rec_value]
    #     print(str(value)[1:-1])
    # # print(end)
    # # print(end[0][1])
    c = 0
    # for i in range(len(end) - 1):
    #     if end[i] == end[i + 1]:
    #         c += 1

    # if c > 0:
    #     print("CONFUSED")
    # else:
    #     print(end[0])

    if most_rec_value == end[1]:
        print("CONFUSED")
    else:
        value = [i for i in freq if freq[i] == most_rec_value]
        print(str(value)[1:-1])