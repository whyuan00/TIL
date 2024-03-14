
from collections import deque
from copy import deepcopy

dir = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(arr):
    q = deque([(0,0)])
    visit = [[0]*M for _ in range(N)]
    newarr = arr.deepcopy()
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni, nj = i+dir[k][0], j +dir[k][1]

            if 0<= ni < N and 0<= nj <M and not visit[ni][nj]:
                # 방문처리
                visit[ni][nj] = 1
                # q에 추가
                q.append((ni,nj))
                # 같은지 확인
                if arr[ni][nj] == arr[i][j] :
                    newarr[i][j] = 0
                    newarr[ni][nj] = 0

    return newarr

newarr = bfs(arr)

for x in range(N): # 각 행의 양끝 확인
    if arr[x][0] == arr[x][M-1]:
        newarr[x][0] = 0
        newarr[x][M-1] = 0

total = 0
for a in range(N):
    for b in range(M):
        total += newarr[a][b]
print(total)