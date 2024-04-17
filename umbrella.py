import sys
sys.stdin = open('input.txt','r')

from collections import deque
from itertools import permutations


def dfs(x,y):
    visit = [[0]*M for _ in range(N)]
    visit[start_i][start_j] = 1
    q=deque([(start_i,start_j)])
    while q:
        i,j = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and not visit[ni][nj] and arr[ni][nj]!='#' and arr[ni][nj]!='E':
                visit[ni][nj] =visit[i][j]+1
                if (ni,nj) == (x,y):
                    return visit[x][y]
                else:
                    q.append((ni,nj))


def count(perm):
    global mincnt, start_i,start_j
    cnt =0
    #perm = ((1, 2), (1, 5), (3, 3), (4, 4))
    for x,y, in perm:
        cnt+= dfs(x,y)-1
        (start_i,start_j) = (x,y)
    mincnt = min(cnt,mincnt)

M, N = map(int,input().split()) # 가로,세로
arr = [list(input()) for _ in range(N)]

start_i=start_j=0
end_i=end_j=0
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            lst.append((i,j))
        elif arr[i][j] =='S':
            start_i,start_j = i,j
        elif arr[i][j] == 'E':
            end_i,end_j = i,j

k = len(lst) # x 좌표개수
mincnt = int(1e9)
# print(lst) [(1, 2), (1, 5), (3, 3), (4, 4)]
x = []
perms = permutations(lst)
for perm in perms:
    perm=list(perm)
    count(perm)

q2= deque([(start_i,start_j)])
visit2 = [[0]*M for _ in range(N)]
while q2:
    i,j = q2.popleft()
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<= nj<M and not visit2[ni][nj] and arr[ni][nj] !='#':
            visit2[ni][nj] = visit2[i][j]+1
            if (ni,nj) ==(end_i,end_j):
                mincnt += visit2[ni][nj]-1
                print(mincnt)
                exit()
            else:
                q2.append((ni,nj))







