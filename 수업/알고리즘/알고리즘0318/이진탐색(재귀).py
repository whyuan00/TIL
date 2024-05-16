def f(key,l,r,dir): # 리스트, 좌, 우, 이전 방향
    global cnt

    if l <= r:
        m=(l+r)//2
        if A[m] == key:
            cnt+=1
            return

        elif A[m] > key:# 왼쪽
            if dir == -1:
                return # 좌-좌
            else:
                f(key,l,m-1,-1)

        else:
            if dir ==1: # 우
                return
            else:
                f(key, m+1,r,1)

    else:
        return

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for i in B: # B에 대한 모든수 탐색
        f(i, 0, len(A)-1,0)
    print(f'#{tc} {cnt}')