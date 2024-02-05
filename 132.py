def bingo(arr):
    total = 0
    sum_diag1 = 0
    sum_diag2 = 0
    for i in range(5):
        sum_row = 0
        sum_col = 0
        for j in range(5):
            #가로
            if arr[i][j] == 0:
                sum_row +=1
            #세로
            if arr[j][i] == 0:
                sum_col +=1

        if sum_row == 5:
            total +=1

        print(sum_col)
        if sum_col == 5:
            total += 1

        if arr[i][i] == 0:
            sum_diag1 +=1

        elif arr[i][4-i] == 0:
            sum_diag1 +=1

    if sum_diag1 == 5:
        total +=1

    if sum_diag2 == 5:
        total +=1


    if total >= 3:
        return True
    else:
        return False

arr = [list(map(int,input().split())) for _ in range(5)]
print(bingo(arr))
