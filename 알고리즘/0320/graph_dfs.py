
# 그래프 형태에 따른 dfs 길찾기
'''
graph = [
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
]
path = []
visit = [0]*5
def dfs(now):
    path.append(now)
    print(now, end=' ')
    visit[now]=1 # 행 방문표시
    for to in range(5):
        if not visit[to] and graph[now][to]:
            dfs(to)
        else:
            continue
dfs(0)
print(path)


'''

'''
graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]

visit = [0]* 5
path = []
def dfs(now):
    for to in graph[now]:
        if visit[to]:
            continue

        visit[to] = 1
        path.append(to)
        dfs(to)
visit[0] = 1
path.append(0)
dfs(0)
print(path)
'''
