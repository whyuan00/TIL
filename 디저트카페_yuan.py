
def f (p, q):
    left = []
    right = []
    x = arr[p][q]

    # 좌대각선 우대각선 미리 리스트에 넣기
    for p1 in range(1, N):
        li, lj = p + dir[0][0] * p1, q + dir[0][1] * p1
        if 0 <= li < N and 0 <= lj < N:
            if arr[li][lj] != x:
                left.append((li, lj))

    for p2 in range(1, N):
        ri, rj = p + dir[1][0] * p2, q + dir[1][1] * p2
        if 0 <= ri < N and 0 <= rj < N:
            if arr[ri][rj] != x:
                right.append((ri, rj))

    # 리스트중 하나라도 비면 False
    if not len(left) or not len(right):
        return False

    else:
        return left, right


# 좌 대각선, 우대각선
dir = [(1,-1),(1,1)]

my = [0,0]

# 없을때는 -1
def dfs(i,j,k):
    global maxcnt

    if k == 2:
        # 시작-> 우 이동만큼 좌에서 이동하면 마지막 좌표
        last_i, last_j = my[0][0]+(my[1][0]-i) , my[0][1]+(my[1][1]-j)
        my.append((last_i,last_j))
        my.append((i,j))





        return

    else:
        for l in left:
            if not my[0]:
                my[0] = l
                dfs(i,j,k+1)
                my[0] = 0

        for r in right:
            if not my[1]:
                my[1] = r
                dfs(i,j,k+1)
                my[1] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 0

    for a in range(N):
        for b in range(N):
            try:
                left, right = f(a,b)
            except:
                continue

            dfs(a,b,0)

    if maxcnt != 0:
        print(f'#{tc} {maxcnt}')
    else:
        print(f'#{tc} -1')