
'''
def dfs(i,m): # i는 현재 넣는 사람
    global res
    if i == M:
        time = max(lst) # 심사대마다 걸린 시간중 가장 큰시간
        if time < res: #그중에서도 가장 작은 시간
            res = time
        return

    if m > res:
        return

    else:
        for j in range(N):
            lst[j] += t_lst[j] # 1번심사대 쓰면 1번 시간 + ...
            if lst[j] > m:
                m = lst[j]
            dfs(i+1, m)
            lst[j] -= t_lst[j] # 원상복구

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    lst = [0] * N # 심사대 리스트 (각 심사대마다 소요한 시간 저장할 것)
    t_lst = [int(input()) for _ in range(N)]

    res = max(t_lst) * M
    dfs(0,0)
    print(f'#{tc} {res}')
'''

'''
# lst[j] += t_lst[j] 일때 max(lst) 가 가장 작아질 수 있는 j 값 찾기  
def f(lst):
    all = []
    for j in range(N):
        lst[j] += t_lst[j]
        time = max(lst)
        all.append((time,j)) # (lst 안의 최대값, 해당 좌표)
        lst[j] -= t_lst[j]

    all.sort(key = lambda x : x[0]) # 최대값이 가장 잘아지도록 정렬
    return all[0][1]


T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    N_lst = [0] * N # 심사대 리스트 (각 심사대마다 소요한 시간 저장할 것)
    t_lst = [int(input()) for _ in range(N)] # N 개의 심사 시간

    t_lst.sort() # 낮은 순서대로 나열, 낮은 순서대로 넣기

    # M - 4번까지만 넣기
    for _ in range(M-4):
        idx = [i for i in range(N) if N_lst[i] == min(N_lst)][0]
        N_lst[idx] += t_lst[idx]

    for _ in range(4):
        min_idx = f(N_lst)
        N_lst[min_idx] += t_lst[min_idx]
        N_lst = N_lst

    print(f'#{tc} {max(N_lst)}')
'''
''' 4천 ms
def dfs(i,sum): # i는 현재 넣는 사람
    global res
    if i == M:
        time = max(lst) # 심사대마다 걸린 시간중 가장 큰시간
        if time < res: #그중에서도 가장 작은 시간
            res = time
        return

    if sum > res:
        return

    else:
        for j in range(N):
            lst[j] += t_lst[j] # 1번심사대 쓰면 1번 시간 + ...
            dfs(i+1, max(lst))
            lst[j] -= t_lst[j] # 원상복구

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    lst = [0] * N # 심사대 리스트 (각 심사대마다 소요한 시간 저장할 것)
    t_lst = [] # 심사대마다 소요시간 저장
    for _ in range(N):
        t = int(input())
        t_lst.append(t)

    res = max(t_lst) * M
    dfs(0,0)
    print(f'#{tc} {res}')
'''