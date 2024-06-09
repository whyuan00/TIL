import sys
sys.stdin = open("input.input","r")

from heapq import heappush,heappop

def dij(start,graph,res):
    pq = []
    pq.append([0,start]) # 누적시간, 시작노드
    while pq:
        t, now = heappop(pq)

        if res[now] <= t:
            continue

        res[now] = t # 시간 업데이트
        for tos in graph[now]:
            time = tos[0]
            to = tos[1]
            heappush(pq,[t+time,to])

T = int(input())
for tc in range(1,T+1):
    N, M, house = map(int, input().split())
    graph1= [[] for _ in range(N+1)]# 노드개수
    graph2= [[] for _ in range(N+1)]# 노드개수

    lst = [list(map(int,input().split())) for _ in range(M)]

    for i in range(M):
        now, to, time = lst[i][0], lst[i][1], lst[i][2]
        graph1[now].append([time,to])
        graph2[to].append([time,now])

    res1=[0]+[int(1e9)]*(N)
    res2=[0]+[int(1e9)]*(N)

    dij(house,graph1,res1)
    dij(house,graph2,res2)

    result = [0]*(N+1)
    for i in range(1,N+1):
        result[i] = res1[i]+res2[i]
    print(f'#{tc} {max(result)}')