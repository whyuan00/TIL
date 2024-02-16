T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 오븐, M 피자
    lst = list(map(int, input().split())) # 치즈 값

    last = 0 # 화덕에 들어간 피자 번호 < M
    size = N + 1 # 큐크기는 하나 더 크게 해주기
    qoven = [0] * (N + 1)  #front = 0 비워놓은 순환큐 오븐
    front = rear = 0

    # N개만큼 오븐에 인덱스 넣기, #(1,N+1)로 안하는 이유는 lst 에서 해당 인덱스로 값 뽑아야 하기때문
    # (1,N+1)로 할거면 lst 에도 [0]+lst 해서 인덱스 맞춰주기
    for i in range(N):
        rear += 1
        qoven[rear] = i
        last += 1

    tmp = -1  # 현재 확인중인 피자(인덱스)
    # 오븐 빌때까지 진행, 마지막으로 확인한 피자 인덱스 tmp 를 프린트할것
    # 넣거나 뺄때 rear 와 front 인덱스 계속 바꿔줘야함

    while front != rear:
        front = (front + 1) % size  #맨처음 투입한거 빼기
        tmp = qoven[front] #tmp에 오븐에 들어갔던 피자인덱스 할당
        lst[tmp] //= 2
        if lst[tmp] > 0:
            rear = (rear + 1) % size #lst 값이 0 아니면 rear+1 에다가 새로넣기
            qoven[rear] = tmp # 넣을 값은 지금 확인 중인 피자인덱스 tmp
        elif  last < M:  # (lst[tmp]<=0 and) 생략되어있음, 치즈 다 녹고 아직 다른 피자 남음 last<M 상황
            rear = (rear + 1) % size
            qoven[rear] = last # 새피자 인덱스 last 넣기
            last += 1  # 피자 인덱스 바꿔주기
    print(f'#{tc} {tmp+1}')  # 인덱스 -> 피자 번호

# def f():
#     while True:
#         for k,v in dic.items():
#             dic[k] = v//2
#             if dic[k] == 0:
#                 if len([v for v in dic.values() if v!= 0]) == 1:
#                     return [k for k,v in dic.items() if v!= 0]
# 
# 
# T = int(input())
# for tc in range(1, T+1):
# 
#     N, M = map(int,input().split())
#     M_lst = [0] + list(map(int,input().split()))
# 
#     N_lst = [i for i in range(1,N+1)]
#     dic = {}
#     for i in N_lst:
#         dic[i] = M_lst[i]  # key는 인덱스, value는 m_lst 의 해당 인덱스 값 , 단 dic에 n개만 넣음
# 
#     # M_lst 의 모든 수를 N_lst에 넣을때까지 v = v//2
# 
#     j = N+1
#     new_dic = {} # 새로 키 추가할 딕셔너리
#     while j < M+1:
#         for k, v in dic.items():
#             dic[k] = dic[k]//2
#             if dic[k] == 0:
#                 if j < len(M_lst):
#                     new_dic[j] = M_lst[j]
#                     j +=1
#                     if len(new_dic) >= N:
#                         break
# 
#     dic.update(new_dic)
# 
#     # 인덱스 전부 넣은 뒤에는 0이 아닌 value가 한개만 남을때까지 value 값 2로 나누기
#     for x in f():
#         result = x
# 
#     print(f'#{tc} {result}')
# 
