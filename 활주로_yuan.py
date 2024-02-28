# 3일때 좌우로 2 나올때 개수 세기 1나오면 break
#좌, 우 , 상, 하
rowdir = [(0,-1),(0,1)]
coldir = [(-1,0),(+1,0)]

# arr ij == 3일때
def f3(i,j,x): # 좌표i,j, 경사로 길이x
    q = []
    q.append((i,j))
    visit = [0] * N
    visit[j] = 1
    while q:
        i, j = q.pop()
        for i in range(2):
            ni,nj = i, j+rowdir[i][1]

            if 0<= ni <N and 0<= nj <N:
                elif arr[ni][nj] == 1:
                    return False

                elif arr[ni][nj] == 3 and not visit[nj]:
                    visit[nj] = 1


                elif arr[ni][nj] == 2 and not visit[nj]:
                    visit[nj] = visit[j]+1
                    q.append((ni,nj))




