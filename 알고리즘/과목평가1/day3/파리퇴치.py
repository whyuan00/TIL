T = int(input())
for tc in range(1,T+1):

    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # f(M) 은 현재위치 (x,y) 로부터 MxM 행렬 더하는 함수
    def f(x,y,M,N,arr):
        total = 0
        for i in range(M):
            for j in range(M):
                    a = x
                    b = y
                    a +=i
                    b +=j
                    if 0 <= a < N and 0 <= b < N:
                        total += arr[a][b]
        return total

    result = 0
    for x in range(N):
        for y in range(N):
            new_result = f(x,y,M,N,arr)
            if new_result > result:
                result = new_result

    print(f'#{tc} {result}')


