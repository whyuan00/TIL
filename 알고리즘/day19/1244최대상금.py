
def f(n):
    global maxnum
    if n == N:
        maxnum = max(maxnum, int(''.join(p)))
        return

    for i in range(p_len-1):
        for j in range(i+1, p_len): # i랑 j 다르게해야 바꾸는 인덱스 다름
            p[i], p[j] = p[j], p[i]

            # 증복숫자 확인
            if int(''.join(p)) not in visit[n]:
                f(n+1)
                visit[n]. append(int(''.join(p)))

            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T + 1):
    p, N = (input().split())  # 123, 1
    p = list(p)  # p는 글자 리스트, N = 교환횟수
    N = int(N)
    p_len = len(p)

    # visited 만들기
    # 바꾸는 횟수만큼 이중리스트 -> 중복값 없앨 것
    visit = [[]for _ in range(N)]
    maxnum = 0
    f(0)
    print(f'#{tc} {maxnum}')




'''
def dfs(i, n):
    global maxsum
    if i == n:
        res = int(''.join(map(str, p)))
        if res > maxsum:
            maxsum = res
        return

    # 백트래킹 추가
    if i > 1 and p[0] not in max_num:
        return

    else:
        for a in range(p_len):
            for b in range(p_len):
                if a!= b:
                    p[a] , p[b] = p[b] , p[a]
                    dfs(i+1, n)
                    p[a] , p[b] = p[b] , p[a]


T= int(input())
for tc in range(1,T+1):
    p, N = (input().split()) #123, 1
    p = list(map(int, p)) #  p는 글자 리스트, N = 교환횟수
    N = int(N)
    p_len = len(p) # 6

    maxsum = 0
    max_num = [p[x] for x in range(p_len) if p[x] == max(p)]

    # p_len 이 더 작은경우 p_len 으로 돌리기
    if p_len <N:
        dfs(0,p_len)
        print(f'#{tc} {maxsum}')

    # N이 더작으면 dfs를 N번만 돌림
    else:
        dfs(0,N)
        print(f'#{tc} {maxsum}')

'''
