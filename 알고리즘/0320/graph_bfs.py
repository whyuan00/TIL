graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]
# bfs 딕셔너리, 데크로 풀기

visit = [0]*5

def bfs(start):
    q = [start]
    visit[start]=1

    while q:
        now = q.pop(0)
        print(now, end=' ')

        for to in graph[now]:
            if visit[to]:
                continue
            visit[to] = 1
            q.append(to)

bfs(0)