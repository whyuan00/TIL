
def f(i,k,s):
    global min_v
    if i == k:
        s = 0
        for j in range(k):
            s += A[j][p[j]]
        if s< min_v:
            min_v = s

    elif s> min_v: #s가 이미 min_v보다 커졌을때는 함수 멈추기
        return

    else:
        for j in range(i,k): # 범위를 i부터로 해줘야함 안해주면 중복으로 나옴
            p[i], p[j] = p[j], p[i]
            f(i+1,k,s+A[i][p[i]])
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = [i for i in range(N)]
    min_v = 1000
    A = [list(map(int,input().split())) for _ in range(N)]
    s = 0
    f(0,N,s) # N까지 찾는 함수 실행
    print(f'#{tc} {min_v}')