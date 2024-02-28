
T = int(input())
for tc in range(1, T+1):
    con, truck = map(int, input().split())
    w = list(map(int,input().split()))
    t = list(map(int,input().split()))

    w.sort(reverse=True) # 무게는 큰순서대로
    t.sort() # 용량은 작은순서대로

    Sum = 0
    for j in range(truck):
        for i in range(con): # 컨테이너가 먼저 바뀌어야함
            if w[i] and t[j] and w[i] <= t[j]: # 둘다 0이 아니고 무게가 용량보다 작을때
                Sum += w[i]
                w[i] = 0
                t[j] = 0

    print(f'#{tc} {Sum}')

