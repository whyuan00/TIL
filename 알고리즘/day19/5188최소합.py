
def f(i,j, now, sum): # 현위치, 레벨, 합
    global minsum
    if now == (N-1)*2:
        if sum < minsum:
            minsum = sum
        return

    else:
        # 우 이동 i, j+1
        if 0<= i < N and 0<= j+1 <N:
           f(i,j+1, now+1, sum+arr[i][j+1])
        # 하 이동 i+1, j
        if 0<= i+1 < N and 0<= j <N:
            f(i+1,j, now+1, sum + arr[i+1][j])


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    minsum = N*N*N

    f(0,0,0,arr[0][0])

    print(f'#{tc} {minsum}')