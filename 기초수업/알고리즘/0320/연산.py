from collections import deque

def bfs(s): #이전까지의연산결과,카운트
    q = deque()
    q.append(s)
    visit = [0] * 1000001
    visit[s] = 1

    while q:
        s = q.popleft()
        if s ==M:
            return visit[s]-1

        if s+1<=1000000 and not visit[s+1]:
            q.append(s+1)
            visit[s+1] = visit[s]+1


        if  s-1>0 and  not visit[s-1]:
            q.append(s-1)
            visit[s-1] = visit[s]+1


        if s*2<=1000000 and not visit[s*2]:
            q.append(s*2)
            visit[s*2] = visit[s]+1


        if  s-10>0 and not visit[s-10]:
            q.append(s-10)
            visit[s-10] = visit[s]+1

    return -1

T = int(input())
for tc in range(1,T+1):

   # N에 연산해서 M 만들기
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N)}')
