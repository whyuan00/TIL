#N*N행렬
# T = 10
# for _ in range(10):

N = 100
tc = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# 왼쪽, 아래, 오른쪽
di = [0, 1, 0]
dj = [-1, 0, 1]
#위치 k는 아래쪽으로 지정


for x in range(N):
    # 현위치 지정
    i, j = 0, x

    while arr[i][j] != 2 and 0 <= i < N and 0 <= j < N:
        k=1
        i = i + di[k]
        j = j + dj[k]

        #현재 좌표 기준 왼쪽 값이 1인경우
        if 0<= j - 1 <N and arr[i][j-1] ==1 :
            #방향전환
            k=2
            while 0<= j - 1 <N and arr[i][j-1] == 1 :
                i = i + di[k]
                j = j + dj[k]


        #현재 좌표 기준 오른쪽 값이 1인경우
        elif 0<= j + 1 <N and arr[i][j+1] == 1 :
            #방향전환
            k = 0
            while 0<= j + 1 <N and arr[i][j+1] == 1 :
                i = i + di[k]
                j = j + dj[k]

    else:
        if arr[i][j] == 2:
            print(x)