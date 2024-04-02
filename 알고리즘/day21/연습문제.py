
# 시간 계산이 어려우면 시간마다 업데이트 하지말고 그때그때 빵을 새로 만들기
# 팔린것만 업데이트
# 빵 개수는 시간 단위로 나눈다음에 정수만큼만 * 빵
'''
def f(lst):

    sold_b = 0
    for i in lst:
        made_b = (i//M) *K # 손님 도착 시점에 만든 붕어: M 으로 나눈 몫 * 붕어

        sold_b +=1 # 팔린 붕어

        if made_b - sold_b <0:
            return 'Impossible'

    return 'Possible'


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())


    N_lst = list(map(int, input().split()))
    N_lst.sort()
    print(f'#{tc} {f(N_lst)}')
'''
# 자기방
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())

    visit= [0] * 400
    maxv =0
    for _ in range(N):
        n, g = map(int, input().split())
        # 문제 최소화 위해 짝수방은 홀수로 올려주기
        if n % 2 == 0:
            n -=1
        if g % 2 == 0:
            g-=1

        if n > g: # 출발지를 더 작게 만들기
            n, g = g, n
        for i in range(n,g+1):
            visit[i] += 1
            maxv = max(visit[i], maxv) # 그때그때 큰걸로 바꿔주기
    print(f'#{tc} {maxv}')
'''
'''
#우, 하, 하 대각선, 좌대각선
dir = [(0,1),(1,0),(1,-1),(1,1)]

def f (i,j):
    for k in range(4): # 4방향 다 동시 검사
        cnt = 1 # 초기화 시점 검토
        for power in range(1,5):
            ni , nj = i+dir[k][0]* power, j+dir[k][1] * power

            if 0<= ni < N and 0<= nj <N:
                if arr[ni][nj]== arr[i][j]:
                    cnt +=1
                if cnt >=5:
                    return True
            else:
                break
    return False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = "NO"
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':
                if f(x,y):
                    ans = 'YES'
    print(f'#{tc} {ans}')

'''     # 상 하 좌 우 /좌측 부터 대각선
dir = [(-1,0),(1,0),(0,-1),(0,1),
       (-1,-1),(-1,1),(1,1),(1,-1)]

def f (i,j,wb): # 현재 좌표, 흑백 색
    arr[i][j] = wb
    for k in range(8):
        wb_lst = []
        for p in range(1,N):
            ni, nj = i+dir[k][0] * p, j+dir[k][1] * p
            if 0<= ni < N and 0<= nj < N:

                if arr[ni][nj] == 0:
                    break

                if arr[ni][nj] == wb:
                    for wbs in wb_lst:
                        arr[wbs[0]][wbs[1]] = wb
                    break

                else:
                    wb_lst.append((ni,nj))
    return



T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # 배열, 돌놓는 횟수

    arr = [[0]* N for _ in range(N)] # N*N 행렬
    arr[N//2 -1][N//2 -1] = 2
    arr[N//2 -1][N//2] = 1
    arr[N//2][N//2 ] = 2
    arr[N//2][N//2 -1] = 1
    for _ in range(M):
        a, b, wb = map(int, input().split())#좌표, 백동
        f(a-1,b-1,wb)

    b_num = 0
    w_num = 0
    for n in range(N):
        b_num += arr[n].count(1)
        w_num += arr[n].count(2)
    print(f'#{tc} {b_num} {w_num}')