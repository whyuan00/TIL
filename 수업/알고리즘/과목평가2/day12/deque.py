'''
덱은 리스트같은 컨테이너
'''

# from collections import deque
#
# q = deque()
# q.append(1) # 넣기
# q.append(2) # 넣기
# # t = q.popleft() # 앞에꺼 꺼내고 지우기.  없으면 indexerror
# print(q.popleft())

from collections import deque
q = deque()
for i in range(1000000):
    q.append(i)
print('append')
while q:
    q.popleft()
print('end')

# list의 pop() 보다 훨씬 빠름
# 덱> 리스트 >선형큐 > 어펜드, 팝