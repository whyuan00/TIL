T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int,input().split()))+[0] for _ in range(N)]

    N +=1 #0인 행과 열 추가
    print(arr)
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] : # ==1이면 True
                cnt += 1
            else:
                if cnt == K:
                    result +=1
                cnt = 0
                # 0이 됐을때 바로 초기화하지말고 이전에 카운트여부 확인
                # 제일마지막에 0넣으면 마지막엔 무조건 확인
                # 그래서 arr에 list + [0]  해서 N range 만들어줌
                # 만약에 if arr[i][j] == or j == N-1로 하면 조건 상세하게 넣어야함 .

        #세로도 봐줘야함
        cnt2
        for j in range(N):
            if arr[j][i] : # ==1이면 True
                cnt2 += 1
            else:
                if cnt2 == K:
                    result +=1
                cnt2 = 0

    print(f'#{tc} {result}')