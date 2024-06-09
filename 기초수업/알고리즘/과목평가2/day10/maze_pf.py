def f(i,j,N):
    st = [] # 지난 경로 저장
    while True:
        maze[i][j] = 1  # 방문 표시  - > 벽으로 메꿔버리기. k_now 만드는 것보다 나음 // 경로 개수셀때는 메꾸면 안됨
        #방문 가능칸 찾기
        #현재칸 기준 상하좌우 찾아서 0이면 st에 저장하고 이동 저장하고 이동을 반복
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i +di, j +dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1: # 벽이 아닐때
                if maze[ni][nj] == 3:
                    return 1
                st.append((i,j)) # 벽 아니면 push
                i, j = ni,nj
                break
        else:
            if st:
                i,j = st.pop()
            else:
                return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    # 시작점 i,j = x,y
    sti = stj = -1
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                sti = x
                stj = y
                break #y
        if sti != -1:
            break #x

    # 미로찾기
    result = f(sti,stj,N)
    print(f'#{tc} {result}')


# 개수 세고 싶으면 3일때 cnt +=1 하고 return 0 을 없애기