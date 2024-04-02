import sys
sys.stdin = open('input.input','r')
from heapq import heappush,heappop

def bfs(start):
    global time_arr
    pq = []
    pq.append([0,start]) # 누적시간, 시작노드,엔드노드
    while pq:
        t, now = heappop(pq)
        if time_arr[start][now] <= t:
            continue

        time_arr[start][now] = t # 시간 업데이트
        for tos in graph[now]:
            time = tos[0]
            to = tos[1]
            heappush(pq,[t+time,to])


T = int(input())
for tc in range(1,T+1):
    N, M, house = map(int, input().split())
    graph= [[] for _ in range(N+1)]# 노드개수

    lst = [list(map(int,input().split())) for _ in range(M)]

    for i in range(M):
        now, to, time = lst[i][0], lst[i][1], lst[i][2]
        graph[now].append([time,to])


    time_arr = [[int(1e9)] * (N + 1) for _ in range(N+1)]
    for i in range(1,N+1):
        if i == house:
            continue
        bfs(i)

    res = [0]*(N+1)
    for i in range(1,N+1):
        res[i] = time_arr[i][house] + time_arr[house][i]
    # print(res)
    print(f'#{tc} {max(res)}')
