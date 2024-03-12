




dir = [(-1,0),(0,1),(1,0),(0,-1)]


def f(x,y,d): # 위치/ 방향
    global cnt
    # 현위치 청소
    if not arr[x][y]:
        arr[x][y] = 1

    # 주변 칸 확인
    check = True
    for k in range(4):
        nx, ny = x+dir[k][0], y+dir[k][1]
        # 청소안된칸 있으면 false 로 바꿔주기
        if 0<=nx<N and 0<=ny<N and not arr[nx][ny]:
            check = False

    #모두 청소시 후진
    if check:
        nx, ny = x-dir[d][0], y-dir[d][1]
        if not (0<=nx<N and 0<=ny<N):
            return
        else:
            cnt+=1
            f(nx,ny,d)
    #하나라도 청소x
    if not check:
        d = (d-1)% 4
        nx, ny = x + dir[d][0], y + dir[d][1]
        if 0<=nx<N and 0<=ny<N and not arr[nx][ny]:
            cnt+=1
            f(nx,ny,d)
        else:
            f(x,y,d)



N, M = map(int, input().split())
x,y,d = map(int, input().split())
arr= [list(map(int,input().split())) for _ in range(N)]
cnt = 0
f(x,y,d)
print(cnt)