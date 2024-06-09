from collections import deque


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # N개 지역
    H = [list(map(int,input().split()))for _ in range(N)]


    visit = [[int(1e9)]*N for _ in range(N)]
    visit[0][0] = 0

    q= deque()
    q.append((0,0))# q에 비용이 갱신된 칸의 인접 인큐 넣어줌
    while q:
        i,j = q.popleft()
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i+di, j +dj
            if 0<=ni<N and 0<=nj<N:
                diff = H[ni][nj]-H[i][j] if H[ni][nj] >=H[i][j] else 0

                # 갱신
                if visit[ni][nj] > visit[i][j]+diff+1:
                    q.append((ni,nj))
                    visit[ni][nj] = visit[i][j]+diff+1


    print(f'#{tc} {visit[N-1][N-1]}')