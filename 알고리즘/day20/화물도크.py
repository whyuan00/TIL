

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work_lst = [list(map(int,input().split())) for _ in range(N)]
    
    work_lst.sort(key = lambda x: x[1]) # 종료시간 기준 sort 
    cnt = 0
    now = 0

    while now != 24:
        for j in range(len(work_lst)):
            work = work_lst[j]
            if work: #작업이 0 아닐때
                now = work[1] # now는 작업의 종료시간
                work_lst[j] = 0 # work 0으로 바꿔주기
                cnt +=1
                break

        for j in range(len(work_lst)):
            work = work_lst[j]
            if work and work[0] < now:
                work_lst[j] = 0

        if work_lst.count(0) == N: # 모든 작업이 0 되면 break
            break
    print(f'#{tc} {cnt}')