def find_starting_position(arr, x):
    left, right = 0, len(arr) - 1
    start_pos = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            start_pos = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return start_pos


def find_ending_position(arr, x):
    left, right = 0, len(arr) - 1
    end_pos = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            end_pos = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return end_pos


def process_queries(N, Q, arr, queries):
    updated_arr = list(arr)

    for query in queries:
        if query[0] == 0:
            i, X = query[1], query[2]
            updated_arr.pop(i - 1)
            updated_arr.insert(i - 1, X)
        else:
            Y = query[1]
            start_pos = find_starting_position(updated_arr, Y)
            end_pos = find_ending_position(updated_arr, Y)

            if start_pos == -1:
                print("-1")
            else:
                print(start_pos + 1, end_pos + 1)


T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    process_queries(N, Q, arr, queries)
