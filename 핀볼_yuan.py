
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(x,y,k,cnt):
    global arr
    global dicworm
    global dicblock
    global maxcnt

    ni = x+ di[k]
    nj = y+ dj[k]
    if 0<= ni < N and 0<= nj <N:

        # 끝내는 조건
        if (ni, nj) == (first_i, first_j):
            maxcnt = max(cnt, maxcnt)
            return

        # 블랙홀
        if arr[ni][nj] == -1:
            maxcnt = max(cnt, maxcnt)
            return

        # 빈공간
        if arr[ni][nj] == 0:
            dfs(ni,nj,k,cnt)
        # 블록
        if 1<= arr[ni][nj] <= 5:
            dfs(ni,nj, dicblock[k][arr[ni][nj]-1] ,cnt+1)
        # 웜홀
        if 6<= arr[ni][nj] <= 10:
            idx = arr[ni][nj]
            if (ni, nj) == dicworm[idx][0]:
                dfs(dicworm[idx][1], k, cnt+1)
            else:
                dfs(dicworm[idx][0], k, cnt+1)

    # 레인지 밖으로 나갈때, 즉 벽에 부딫힐때
    else:# 상,하,좌,우  -> 반대로 방향 하, 상, 좌, 우가기
        if ni <0:
            dfs(ni+1, nj, 1, cnt+1)
        elif ni >=N:
            dfs(ni-1, nj, 0, cnt+1)
        elif nj <0:
            dfs(ni, nj+1, 2, cnt+1)
        elif nj >=N:
            dfs(ni, nj-1, 3, cnt+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 0

    # 블록 만날때 #k= 1,2,3,4, / 블록이 1,2,3,4,5 -> 5개씩
    dicblock = [ [2,2,1,3,2], [0,3,3,2,3], [3,1,0,0,0], [1,0,2,1,1] ]

    # 웜홀 #k= 1,2,3,4, / 블록이 6,7,8,9,10 -> 5개씩
    key = [i for i in range(6, 11)]
    value = [[] for _ in range(5)]
    dicworm = dict(zip(key, value))

    # 웜홀 넣기
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                dicworm[arr[i][j]].append((i, j))

    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:
                for k in range(4):
                    first_i, first_j = i, j
                    dfs(i,j,k,0)

    print(f'{tc} {maxcnt}')

