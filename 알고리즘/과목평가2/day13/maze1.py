def bfs(s):
    q = []
    q.append(s)
    ved = [[0]*16 for _ in range(16)]
    i,j = s
    ved[i][j] = 1 # 방문

    while q:
        i, j = q.pop(0)
        if arr[i][j] ==3:
            # print(i,j)
            return 1
        for di in ([1,0,-1,0]):
            for dj in ([0,1,0,-1]):
                ni = i +di
                nj = j +dj
                if 0<=ni<16 and 0<=nj<16 and not ved[ni][nj] and arr[ni][nj] !=1:
                    ved[ni][nj] = 1
                    q.append((ni,nj))
    return 0

T = 10
for _ in range(1,11):
    tc = int(input())
    arr = [list(map(int,list(input()))) for _ in range(16)]

    x=y = 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] ==2:
                x,y = i,j
    s = (x,y)
    # bfs(s)
    print(f'#{tc} {bfs(s)}')