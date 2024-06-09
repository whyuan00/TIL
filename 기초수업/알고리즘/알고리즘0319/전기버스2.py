

def dfs(i,s,cnt,j): #현재 정류장인덱스, s는 현재 배터리 용량, 충전횟수, 직전충전위치
    global mincnt

    #도착했을때
    if i== N:
        mincnt = min(cnt,mincnt)
        # print(path)
        return

    if cnt > mincnt:
        return

    #현재정류장이 이전 충전 번호 +s 보다 큰경우
    if i+1 > j+1+s:
        return

    #충전 안하고 다음으로 넘어가기
    dfs(i+1,s,cnt,j)

    #충전하고 다음으로 넘어가기
    dfs(i+1,lst[i],cnt+1,i)

T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    N = lst.pop(0)
    lst = lst+[0]
    # 시작점 i = 0, s = 1, j = -1
    mincnt = N-1

    dfs(0,1,0,-1)
    # print(mincnt-1)
    print(f'#{tc} {mincnt-1}')