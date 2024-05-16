'''
최단경로: 두 정점사이 경로중 가중치합이 최소인 경로
* 트리와 차이 주의, 트리와 달리 모든 노드 방문안해도 됨

- 다익스트라( 음은x
- 벨만 포드(음가중치 허용
- 플로이드-워샬 (모든정점에 대한 경ㄹ
'''
# 다익스트라 알고리즘
'''
거리가 최소인 정점 선택하면서 최단경로
시작에서 끝까지의 최단경로에 정점x 존재
최단경로는 s에서 x까지의 최댄경로와 x에서 t까지의 최단경로로 구성

'''
from heapq import heappush,heappop

INF = int(1e9) # 거리에 넣어둘수

V, E = map(int, input().split())
start = 0 # 시작노드 알려줄것, 방향있는 경우 있음
graph = [[]for _ in range(V)]

# s누적거리 저장변수
distance = [INF] * V

# 간선정보저장
for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append([w,e]) # s노드에서는 e로 w만큼 갈수있음

def dijkstra(start):
    pq = []
    # weight와 노드 저장
    heappush(pq,(0,start))
    # 시작점 0으로 초기화
    distance[start] = 0

    while pq:
        # 최단거리 노드로 나옴
        dist, now = heappop(pq)
        print(dist,now)

        # 더 긴거리가 미리 저장되어있음,
        # now가 이미 더 짧은 거리로 온적있다면 pass
        if distance[now] < dist:
            continue

        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            #  누적 dist 갱신할지 확인
            new_dist = dist+ next_dist
            if new_dist>= distance[next_node]:
                continue
            distance[next_node] = new_dist
            heappush(pq,(next_dist,next_node))

dijkstra(0)
print(distance)