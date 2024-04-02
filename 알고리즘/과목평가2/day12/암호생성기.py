
from collections import deque

for _ in range(8):
    tc = int(input())
    lst = list(map(int, input().split()))
    dq = deque(lst)

    def f():
        while True:
            for i in range(1, 6):
                x = dq.popleft()
                if x - i > 0:
                    dq.append(x - i)
                else:
                    dq.append(0)

                    return dq

    f()
    print(f'#{tc}', end = ' ')
    for x in dq:
        print(x, end = ' ')
    print()

# while True:
#     for i in range(1,6):
#         x = dq.popleft()
#         if x - i >0:
#             dq.append(x-i)
#         else:
#             dq.append(0)
#             print (dq)
#


# 원형큐 하면 메모리 에러
#
# def enq(x):
#     global rear
#     rear = (rear +1) % N
#     q[rear] = x
#
# def delq():
#     global front
#     global rear
#     if front == rear:  #isempty
#         return False
#     else:
#         front = (front +1) % N
#         return q[front]
#
# rear = front = -1
#
# lst = [10239, 10248, 10242 ,10240, 10242, 10242 ,10245 ,10235]
# N = len(lst)
# q= [0] * (N) # 선형큐
#
# for i in lst:
#     enq(i)
#
# while True:
#     for i in range(1,6):
#         x = delq()
#         if x-i > 0:
#             q.append(x-i) # 넣기
#             rear +=1
#
#         else:
#             q.append(0)
#             rear +=1
#             exit()
#
# print(q[front+1:])




# 재귀로 풀면 recursion error
# def f(dq):
#     for i in range(1,6):
#         x = dq.popleft()
#         if x - i >0:
#             dq.append(x-i)
#         else:
#             dq.append(0)
#             return dq
#
#     return f(dq) # for문 5번 다 돈뒤에도 음수값 안나오면 다시 돌기
#
#
# from collections import deque
#
# lst = list(map(int, input().split()))
# dq = deque(lst)
#
# print(f(dq))