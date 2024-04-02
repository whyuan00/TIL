'''
BFS는 너비우선탐색
근거리의 지점을 모두 확인
그다음의 근거리를 모두 확인
'''

N = int(8)
G= [1,2,3,4,5,6,7,8] # 그래프
visited = [False for _ in range(N+1)]
print(visited)

Q = [] # Q는 빈곳으로 생성
v = G[0]
Q.append(v) # 시작점 넣기

while Q:
    t = Q.pop(0) # 첫번째꺼 빼기
    if not visited[t]:
        visited[t] = True
        #visit(t)
        for i in G[t]: #t 의 인접점에 대해서 방문 안한 지점은 전부 넣기
            if not visited[t]:
                Q.append(i)
