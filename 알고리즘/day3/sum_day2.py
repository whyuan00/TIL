T = 10
for tc in range(1, T+1):
    a = int(input())
    arr = [input().split() for _ in range(100)]

    max_row_sum = 0
    max_column_sum = 0
    for i in range(10):
        row_sum = 0
        column_sum = 0

        for j in range(10):
            row_sum += arr[i][j]
            column_sum += arr[j][i]

        if row_sum > max_row_sum:
            max_row_sum = row_s
        if column_sum > max_column_sum:
            max_column_sum = column_sum

    max_diag_sum = 0
    for i in range(10):
        diag_sum = 0
        for j in range(10):
            diag_sum += arr[i][i]
            diag_sum += arr[j][10-j]
        if diag_sum >max_diag_sum:
            max_diag_sum = diag_sum

    result = max(max_diag_sum, max_row_sum, max_column_sum)

    print(f'#{tc} {result}')
