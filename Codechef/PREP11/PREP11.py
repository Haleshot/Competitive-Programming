def is_allocation_possible(books, students, max_pages):
    students_needed = 1
    pages_allocated = 0

    for pages in books:
        if pages > max_pages:
            return False

        if pages + pages_allocated <= max_pages:
            pages_allocated += pages
        else:
            students_needed += 1
            pages_allocated = pages

    return students_needed <= students

def allocate_books(books, students):
    low, high = max(books), sum(books)
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if is_allocation_possible(books, students, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

T = int(input())
for _ in range(T):
    N, A = map(int, input().split())
    books = list(map(int, input().split()))

    # Find the minimum value for the maximum sum of pages
    result = allocate_books(books, A)
    print(result)
