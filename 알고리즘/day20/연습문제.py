# 바이너리 카운팅
# 친구abcd 중 2명 이상의 친구 선정해서 함께 카페 가려고 할경우 몇가지?


# abcde => n = 1,2,3,4,5 / 부분집합 만들어서 수가 2명이상일때만 카운트 +1
'''
arr = ['a','b','c','d','e']
N = len(arr)

def f(tar):
    for i in range(N):
        if tar & 0x1: # 타겟과 10진수 1을 이용해서 마지막자리가 1인지 0인지 검사
            print(arr[i], end = '') # 끝자리가 1이면 프린트
        tar >>= 1 # tar 을 한번더 밀어주기

f(6)  # 6은 비트로 0b110, f(tar) 에서 tar 의 마지막 자리가 1인지 0인지 검사하는 문제
# 110 이면 bc 가 출력됨
'''

# n = 5
# cnt = 0
# for i in range(1<<n):
#     s = []
#     for j in range(n):
#         if i & (1<<j):
#             s.append(arr[j])
#     if len(s) >= 2:
#         cnt +=1
#
# print(cnt)

'''
arr =  ['a','b','c','d','e']
n = len(arr)
def f(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1: # 가독성을 위해 0x1로써줌  0x1은 16진수
            cnt +=1 # tar의 bit가 1이면 카운트
        tar >>=1 # tar 을 하나 오른쪽으로 밀어줌
    return cnt # tar 밀면서 bit 있을때마다 cnt +1ㅠ+1

res = 0
for x in range(1<<n):
    if f(x) >= 2:
        res +=1
print(res)

'''

# 재귀호출로 조합 만들기
# 5명중 k명 뽑아서 조합만들때?
# branch 는 5, lv = 3
'''
arr =  ['a','b','c','d','e']
N = len(arr) 
k = 3 #3명 뽑는다고 가정


path = []
def find(lv, i):
    if lv == k:
        return
    
    else:
        for j in range(i,N):
            path.append(arr[j])
            find(lv+1, i+1)
            path.pop()
'''

# 조합: 주사위 k개에서 나올수 있는 모든 조합 출력
'''
N = 3
path = []

def f(lv, start):

    if lv == N:
        print(path)
        return

    for i in range(start,7):
        path.append(i)
        f(lv+1, i) # 세개 주사위니까 각각 독립시행, 111 112, 222, ...
        # i+1 로 하면 숫자 중복없이 하는거, 한개 주사위->수열
        path.pop()

f(0,1)
'''
# 화장실 문제 그리디? :  시간 작은 순 정렬
'''
n = [15,30,50,10]
n.sort()
N = len(n)

sum = 0
for i in range(N):
    sum += (N-1-i) *  n[i]
print(sum)
'''

# 키로당 가격 그리디
'''
n = 3
target = 30
things = [(5,50), (10,60), (20,120)]
things .sort(key = lambda x : x[1]/ x[0], reverse = True)
'''


