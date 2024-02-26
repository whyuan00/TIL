def bfs(s,g,v):
    q = []
    visited = [0] * (v+1)
    visited[s] = 1
    q.append(s)

    while q:
        # 현재위치 i
        i = q.pop(0)
        if i == g:
            return visited[i] -1

        #인접점 찾기
        for x in adjl[i]:
            if visited[x] ==0:
                visited[x] = visited[i] +1
                q.append(x)

T = int(input())
for tc in range(1,T+1):

    v, E = map(int, input().split())
    adjl = [[]*v for _ in range(v+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        adjl[i].append(j)
        adjl[j].append(i)

    # 출발, 도착
    s,g= map(int, input().split())

    # bfs(s, g, v)

    print(f'#{tc} {bfs(s,g,v)}')
