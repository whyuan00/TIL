T = int(input())
for tc in range(1,T+1):

    N, M = map(int, input().split()) # N번째 비트까지 모두 1인지 확인

    #N개만큼 1 인 비트 만들기
    b = (1<<(N)) - 1 # 1+N 이면 자리수는 N+1 이됨 주의

    if M & b == b:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')
