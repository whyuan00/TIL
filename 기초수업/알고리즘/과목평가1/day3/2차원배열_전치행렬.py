#전치행렬이란 대각선 기준으로 왔다갔다 하는거
# 대각선 위는 열이 이동하니까 j>i , 아래는 행이 이동하니까 i>j

arr = [[1,2,3], [4,5,6],[7,8,9]] # 33행렬

for i in range(3):
    for j in range(3):
        if j>i:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
