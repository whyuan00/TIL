# dfs 로 각 조에 한명씩 N번 반복해서 넣어주는 여러 경우
def dfs(current, i):




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = []
    B = []
    min_sum = 0
    dfs(1,0) # 현재 번호, 카운트 수
    print(f'#{tc} {min_sum}')






