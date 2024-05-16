import sys
sys.stdin = open("input.input","r")




d = [(0,1),(0,-1),(1,0),(-1,0)]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = [0]*(N**2+1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni,nj = i+d[k][0], j+d[k][1]
                if 0<=ni<N and 0<= nj<N and arr[ni][nj]==arr[i][j]+1:
                    count[arr[i][j]]= 1

    maxcnt = 0
    cnt = 1
    start = 0
    for i in range(N**2,-1,-1):
        if count[i]:
            cnt+=1
        else:
            if cnt>=maxcnt:
                if cnt ==maxcnt:
                    start = min(start,i+1)
                else:
                    start = i+1
                maxcnt = cnt
            cnt= 1
    print(f'#{tc} {start} {maxcnt}')






'''

#모든 방 다가기 / 상하좌우 중에 갈곳이 없을때 max 바꾸고 리턴
def dfs(start,i,j,cnt): #현재 좌표/ 확인한 방개수(이동홧수)
    global maxcnt,res,visit

    if (N**2 - visit) + cnt < maxcnt:
        return

    check = False
    for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == arr[i][j]+1 :
            check = True
            dfs(start,ni,nj,cnt+1)
        visit+=1

    if not check:
        if cnt == maxcnt:
            maxcnt = cnt
            res = min(res,start)
        if cnt > maxcnt:
            maxcnt = cnt
            res = start
        return




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    maxcnt = 0
    visit = [[0]*(N+1) for _ in range(N+1)]
    res = N
    # 시작좌표
    for i in range(N):
        for j in range(N):
            visit=0
            dfs(arr[i][j],i,j,0)
    print(f'#{tc} {res} {maxcnt+1}')
'''
