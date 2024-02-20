

# 각 열에 대해 연속성 검사 함수
def find(row,col,arr,k):
    k_row = [False for _ in range(col)]
    for i in range(col):
        cnt = 1
        for j in range(1, row):
            if arr[j - 1][i] == arr[j][i]:
                cnt += 1

            elif arr[j - 1][i] != arr[j][i]:
                if cnt >= k:
                    k_row[i] = True
                cnt = 1
            if j == row - 1:  # 마지막 열은 항상 체크
                if cnt >= k:
                    k_row[i] = True
    if k_row.count(False) == 0:
        return True
    else:
        return False

# dfs
def change(arr,n,idx):
    global min_cnt
    print(n)
    if n >= min_cnt or idx == row:
        return

    elif find(row,col,arr,k):
        print(arr, n,idx)
        if min_cnt > n:
            min_cnt = n

    # 반복횟수가 min보다 커지거나 행만큼 다하면 return
    else:
        #dfs
        for j in range(idx,row):
            test = []
            test.extend(arr)
            change(arr,n,j+1) # 행렬 안바꾸고 idx 만 바꿔서 넣기

            # test.extend(arr) # 원상복구위한  test
            arr[j] = [0] * col # 행렬 0으로 바꾸기
            change(arr,n+1,j+1)

            arr = test
            arr[j] = [1] * col # 행렬 1로 바꾸기
            change(arr,n+1,j+1)
            # # 원상복구

            arr = test

# T = int(input())
# for tc in range(1,T+1):
row, col, k = map(int,input().split()) # 두께6, 너비8, 합격기준
arr = [list(map(int,input().split())) for _ in range(row)]
min_cnt = row  # 최대횟수는 행 수

# arr의 한줄씩 바꾸기, 두줄 바꾸기, 세줄바꾸기... bit로 풀기
change(arr,0,0)

# print(find(row,col,arr,k))