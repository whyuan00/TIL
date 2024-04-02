T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    # 행렬 가로세로 맨 끝에 0 하나 추가하기
    arr = [list(map(int, input().split()))+[0] for _ in range(N) ] + [[0] * (N+1)]

    #추가한 0 N값에 반영 ( N+1 행렬)
    N += 1

    #최종 값
    result = 0
    cnt1 = 0
    cnt2 = 0

    # 가로 자리 확인
    for i in range(N):
        for j in range(N):
            # 0일때 카운트 확인, 확인후 cnt 초기화
            if arr[i][j] == 0:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            else:
                cnt1 += 1

    # 세로 자리 확인
    for i in range(N):
        for j in range(N):
            # 0일때 카운트 확인, 확인후 cnt 초기화
            if arr[j][i] == 0:
                if cnt2 == K:
                    result += 1
                cnt2 = 0
            else:
                cnt2 += 1

    print(f'#{tc} {result}')