# 원형 큐로 풀기

def isfull():
    return (rear+1) % len(Q) == front

def isempty():
    return rear == front

# 원형 큐의 삽입 (맨뒤에 넣음 => 현재rear +1 을 원형큐로 나눈 나머지)
def enq(x):
    global rear
    if isfull():
        return
    else:
        rear = (rear +1) % len(Q)
        Q[rear] = x

# 원형 큐의 삽입 (맨뒤에 넣음)
def delq(x):
    global front
    if isempty():
        return
    else:
        front = (front + 1) % len(Q)
        return Q[front]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    q = list(map(int,input().split()))

    # 맨뒤로 보내는 작업 최소화
    # m 은 뒤로 보내야할 수
    m = M % N

    # 원형큐 Q 생성
    Q = [0] * (N+1)
    rear = front = -1

    # 원형큐에 q 넣기
    for i in q:
        enq(i)

    #원형큐의 첫번째수 뒤로보내기 m번반복
    for _ in range(m):
        x = Q[0]
        delq(x)
        enq(x)

    print(f'#{tc} {Q[front+1]}') # 큐에서 제일 첫번째 원소 위치는 front +1 (마지막으로 뺀자리 +1)



#
# #q의 수를 m 번 뒤로 보냄
#
# cnt = 0
# while cnt != m:
#     t = q.pop(0)
#     q.append(t)
#     cnt +=1
# print(q[0])