
'''
V E : v는 1부터 v까지 점, e개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s,n):
    Q = []
    visited = [False for _ in range(n+1)]

    Q.append(s) # 시작점 추가
    visited[s] = True

    # Q 가 비워질때까지 방문
    while Q:
        t = Q.pop(0)
        # t에서 할일하기
        print(t)
        for i in adjl[t]:
            if not visited[i]:
                Q.append(i)
                visited[i] = True
    print(visited)



V, E = 7, 8 #map(int,input().split())

arr = [1, 2, 1, 3 ,2 ,4 ,2, 5 ,4 ,6 ,5 ,6 ,6 ,7, 3 ,7]#list(map(int,input().split()))

adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[2*i], arr[2*i +1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

bfs(4,V)


# 스웨아
def bfs(s,n,G) # 시작점, 노드개수, 도착점 G
    q = []
    visited = [0] * (n+1)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == G:
            return visited[t]-1 # 도착했을때 그동안 지나간 수 리턴
        for i in adjl[t]:
            if not visited[t]:
                q.append(i)
                visited[i] = visited[t] +1 # visited 에 몇개 경로 지나갔는지 넣기
    return 0

adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[2*i], arr[2*i +1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

bfs(시작점, v, 도착점) # v 는 노드 개수