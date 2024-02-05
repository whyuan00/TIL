# 3줄 이상 빙고인지 구하는 함수
def bingo(arr):
    total = 0
    sum_diag1 = 0
    sum_diag2 = 0
    for i in range(5):
        sum_col = 0
        for j in range(5):
            #가로
            if arr[i] == [0,0,0,0,0]:
                total +=1
            #세로
            elif arr[j][i] == 0:
                sum_col +=1

        if sum_col == 5:
            total +=1

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
N = 5
# 빙고판
arr1 = [list(map(int,input().split())) for _ in range(N)]
# 사회자
arr2 = [list(map(int,input().split())) for _ in range(N)]



# 25개 일렬로 된 리스트 만들기
arr2new = []
for x in arr2:
    arr2new.extend(x)


# arr1[i][j] 가 arr2new의 x 와 같을때 0으로 바꾸기
# 0으로 바꿀때마다 arr1이 빙고인지 확인. 빙고일때의 x  인덱스 출력

def f(arr1,arr2new):
    for x in arr2new:
        for i in range(5):
            for j in range(5):
                if arr1[i][j] == x:
                    arr1[i][j] = 0
                    if bingo(arr1):
                        result = arr2new.index(x) + 1
                        return result

print(f(arr1,arr2new))





