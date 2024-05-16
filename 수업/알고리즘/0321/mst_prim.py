'''
mst: 최소 신장 트리
1. 프림 알고리즘
2. 크루스칼 알고리즘
'''


# 프림
'''
임의정점 하나 선택해서 최소비용간선만 선택 -> 우선순위 큐로 구현현
1. 갈수있는 경로 다 넣어주기, 그중에 제일 작은거 선택 
2. 막히면 직전에서 새로운 경로 꺼내오기 


import sys
sys.stdin = open("input.txt","r")
'''

from heapq import heappush,heappop

def prim(start):
    pq = []
    mst = [0]*V #
    # 최소비용 _가중치의 합 저장
    sum_weight = 0
    # 시작점 추가 _ 기존 bfs 는 노드번호만 관리
    # 프림은 우선순위가 가중치에 따라 정렬되어야함(가중치낮으면 먼저나옴)
    # 관리해야할데이터는 가중치, 노드번호
    # 동시에 두개 다루기: class로 만들기 /
    heappush(pq,(0,start)) # 튜플아닌 class 로도 가능 class node, self.name, self.weight

    while pq:
        weight, now = heappop(pq)

        # 같은지점 방문시 continue
        # bfs 는 다방문
        # 프림과 bfs차이: 프림은 일단  pq에 넣지만 방문은x
        # 더 먼거리로 가는방법이 큐에 저장되어있으
        # 더 짧은 거리로 이미 방문했다면 안감
        if mst[now]:
            continue

        print(now, mst)
        # 방문처리
        mst[now]=1
        #누적합 추가
        sum_weight += weight

        # 갈수있는노드 보면서
        for to in range(V):
            # 갈수없음/이미 방문시
            if not graph[now][to] or mst[to]:
                continue
            heappush(pq,(graph[now][to],to))

    print(f'최소비용: {sum_weight}')


V, E = map(int, input().split())
# 인접행렬로 저장( 실습시간에는 인접리스트저장)

graph = [[0]* V for _ in range(V)]

for _ in range(E):
    s,e,w = map(int,input().split())
    # 가중치 그래프 3-> 4 로 가는데 31 비용듦
    #graph[3][4] = 31
    graph[s][e] = w
    graph[e][s] = w #무방향그래프프

prim(0)