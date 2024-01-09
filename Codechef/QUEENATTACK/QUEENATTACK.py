T = int(input())
while T:
    T -= 1
    N, X, Y = map(int, input().split())
    cells_in_row_column = (N - 1) * 2
    cells_in_diagonals = min(N - X, N - Y) + min(X - 1, Y - 1) + min(N - X, Y - 1) + min(X - 1, N - Y)
    cells_under_attack = cells_in_row_column + cells_in_diagonals

    print(cells_under_attack)