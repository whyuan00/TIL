di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 꽃가루 개수
    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선 꽃가루 수

            for q in range(1, arr[i][j]+1):  # 가운데 풍선 개수 q 만큼 상하좌우 터트리기 반복
                for k in range(4):
                    ni = i + di[k] * q
                    nj = j + dj[k] * q
                    if 0<= ni <N and 0<= nj <M:
                        cnt += arr[ni][nj]


        # 최대수 구하기
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')