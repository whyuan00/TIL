
#델타 우 하 좌 상
di = [0,1,0,-1]
dj = [1,0,-1,0]

def f(i,j,k_now,arr):
    st = []
    # 0따라 위치 이동
    while True:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0<= ni< N and 0<= nj <N and arr[ni][nj] != '1':
                if arr[ni][nj] == '3':
                    return 1

                if k!= k_now:
                    st.append((ni,nj,k))
                    i , j, k_now = ni, nj, k  #간길 스택에 넣어주기
                    break

        else:
            if st:
                i, j, k_now = st.pop()

            else:
                return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 시작점 i,j = x,y
    i = j = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == '2':
                i=x
                j=y
                break
            break

    #초기 k_now값 0 아닌걸로 아무거나지정
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni< N and 0<= nj <N and arr[ni][nj] != '0':
            k_now = k
            break

    print(f'#{tc} {f(i,j,k_now,arr)}')
