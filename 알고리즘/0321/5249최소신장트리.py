# from heapq import heappush,heappop

def findset(x):
    if p[x] == x:
        return x

    p[x] = findset(p[x])
    return p[x]

def union(x,y):
    x = findset(x)
    y = findset(y)
    if x==y:
        return
    elif x > y:
        p[x] = y
        return
    elif x < y:
        p[y] = x
        return



# kruskal은 최소거리부터 가되, 싸이클이면 가지않음


T = int(input())
for tc in range(1,T+1):
    #마지막 노드, 간선개수
    V, E =map(int, input().split())

    # 노드확인할거라 가중치행렬말고 노드 연결로 받기
    # graph = [[]for _ in range(V+1)]
    p = [i for i in range(V+1)] # union 체크할 것
    pq = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        # graph[n1].append(n2)
        # graph[n2].append(n1)
        # pq에 가중치 작은 순서대로 연결 노드
        pq.append([n1,n2,w])
    pq.sort(key=lambda x: x[2]) # 무게 작은순으로 sort
    sum_weight = 0
    cnt = 0

    for n1,n2,w in pq:
        if findset(n1) == findset(n2): #이미 연결되있으면pass
            continue
        union(n1,n2) # n1과 n2 중 find가작은 수로 연결
        cnt+=1
        sum_weight+= w
        if cnt == V:
            break
    # print(sum_weiht)
    print(f'#{tc} {sum_weight}')


'''
def prim(start):
    global sum_weight
    mst = [0]* (V+1)
    pq = []
    heappush(pq,(0,start)) # 가중치, 노드
    while pq:
        w, now = heappop(pq) # 꺼내기
        if mst[now]:
            continue # 이미 방문했으면 continue

        mst[now] = 1
        sum_weight += w

        for to in range(V+1):
            # 방문안한노드, 가중치가 있는 노드
            if graph[now][to] and not mst[to]:
                # pq에 가중치와 다음 노드 넣기
                heappush(pq,(graph[now][to], to))






T = int(input())
for tc in range(1,T+1):
    # 노드개수, 간선 개수
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    # prim: 작은 거리부터 가되 방문처리
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
    sum_weight = 0
    # 그래프에 가중치로 다 넣음
    prim(0)
    # print(sum_weight)
    print(f'#{tc} {sum_weight}')
'''
