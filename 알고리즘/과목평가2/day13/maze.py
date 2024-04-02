from collections import deque

def bfs(i,j):
    #  큐 q 는 데크
    q = []
    q = deque(q)
    q.append((i,j))
    visited = [[0] *N for _ in range(N)]
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        if arr[i][j] == 3:
            return visited[i][j] -2

        # 인접지역 탐색해서 큐에 넣어주기
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and not visited[ni][nj]: # 인접지역의 방문 안한 수는
                    visited[ni][nj] = visited[i][j]+1 # 방문 표시
                    q.append((ni,nj))
        # appendleft 를 하면 깊이탐색이 됨, 너비탐색을 할때는 최단 경로거리를 구할수 있으나
        # 깊이 탐색하면 내가 찾은 경로가 최단 거리가 아닐수 있음

    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,list(input())))for _ in range(N)]

    # 델타 우하좌상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    #시작점 i, j
    i=j=0
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 2:
                i, j = a, b
# bfs(i, j)
    print(f'#{tc} {bfs(i,j)}')
