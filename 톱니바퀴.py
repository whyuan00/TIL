from collections import deque


def dfs(n,d,visit,k):  # 현재 돌리는 바퀴번호/돌리는 방향/ visit/총 돌린 횟수
    if k==4:
        return # 4번 돌리면 return
    else:
        # 방문안한 바퀴만 돌리기
        if not visit[n-1]:
            visit[n-1] = 1
            # 돌리기
            if d==1: # 시계방향
                t = wheel[n-1].pop()
                wheel[n-1] = wheel[n-1].appendleft(t)

            else: # 반시계 방향
                t = wheel[n-1].popleft()
                wheel[n-1].appendleft(t)

        if 1<n<=3: # n 이 2or3or 4일때
            #앞에 바퀴돌리기
            if wheel[n-1][6] != wheel[n-2][2]:
                dfs(n-1,-d,visit,k+1)

            #뒤에 바퀴 돌리기
            if wheel[n-1][2] != wheel[n][6]:
                dfs(n+1,-d,visit,k+1)
            else:
                return

        elif n==1:
            # 뒤에 바퀴 돌리기
            if wheel[n - 1][2] != wheel[n][6]:
                dfs(n + 1, -d, visit, k + 1)
            else:
                return
        elif n==4:
            # 앞에 바퀴돌리기
            if wheel[n - 1][6] != wheel[n - 2][2]:
                dfs(n - 1, -d, visit, k + 1)
            else:
                return

wheel = []
for n in range(4):
    wh = input()
    x = deque([]) # 톱니바퀴 한줄씩 데크임
    for i in wh:
        x.append(int(i))
    wheel.append(x)
k = int(input()) # k는 회전 횟수
for _ in range(k):
    n, d = map(int, input().split()) # 톱니번호, 방향
    visit=[0]*4
    dfs(n,d,visit,0) # 현재 돌리는 바퀴번호/돌리는 방향/ 총 돌린 횟수

for j in wheel:
    print(j)
print()