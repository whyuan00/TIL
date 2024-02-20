from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])
idx = [] # 시간줄이려면 인덱스 최대한 간소화 : 앞은 1 뒤는 0
tmps = [input().strip() for _ in range(N)]
# print(tmp) # ['1 a', '2 b', '1 c', '3', '3']

for tmp in tmps:
    if '1' in tmp:
        q.append(tmp[-1])
        idx.append(0) # 뒤
    elif '2' in tmp:
        q.appendleft(tmp[-1])
        idx.append(1) # 앞
    elif q and '3' in tmp:
        if idx.pop(): # idx pop 한게 1이면  앞에꺼 빼기
            q.popleft()
        else:
            q.pop() # idx pop 이 0이면 뒤에꺼 빼기
if q:
    print(''.join(map(str,q)))
else:
    print(0)



'''시간초과 
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])
res = ''

for _ in range(N):
    x = input()
    if q and '3' in x:
        q.pop()
    else:
        q.append(x)

for lst in q:
    if '1' in lst:
        res = res + lst[-1]

    elif '2' in lst:
        res = lst[-1]+ res

if res:
    print(res)
else:
    print(0)
'''
