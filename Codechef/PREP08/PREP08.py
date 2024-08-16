def is_painting_possible(walls, painters, time_per_unit, max_time):
    total_time = 0
    painters_needed = 1

    for wall in walls:
        if wall * time_per_unit > max_time:
            return False

        if total_time + wall * time_per_unit <= max_time:
            total_time += wall * time_per_unit
        else:
            painters_needed += 1
            total_time = wall * time_per_unit
    return painters_needed <= painters


def minimum_painting_time(walls, painters, time_per_unit):
    low, high = max(walls) * time_per_unit, sum(walls) * time_per_unit
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if is_painting_possible(walls, painters, time_per_unit, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    walls = list(map(int, input().split()))

    # Find the minimum time required to paint N walls
    result = minimum_painting_time(walls, A, B)
    print(result)
