
'''
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            for q in range(1,4):
                print(i,j,k,q)
'''

# brance = 2, level = 3
# 재귀
'''
def f(x):
    if x == 3:
        return
    else:
        f(x+1)
        f(x+1)

f(0)
'''
# 중복순열 + 방문흔적(path) 남기기
# 012 중복순열 만들때
#level2, branch3
'''
path = []

def kfc(x):
    if x == 2: #level
        print(path) # 종료 직전에 출력코드
        return
    else:
        for i in range(3): #branch
            # 값복사하기
            path.append(i)
            kfc(x+1)
            path.pop() # 되돌아온후 이전기록 삭제해서 새로운 패스만 뱉기
kfc(0)
'''

#brnch 6 #level 3
# 111 ~ 666
'''
path = []
def kfc(x):
    if x == 3:
        print(' '.join(map(str,path)))
        return
    else:
        for i in range(1,7):
            path.append(i)
            kfc(x+1)
            path.pop()
kfc(0)
'''

# 11111 44444 : 레벨 5, 브랜치 4
'''
path = []
def kfc(x):
    if x == 5:
        print(path)
        return
    else:
        for i in range(1,5):
            path.append(i)
            kfc(x+1)
            path.pop()
kfc(0)
'''
# 중복순열 제거 _ 0을 이미 선택하고 재귀호출시 다시 0 선택 못하게.
# visit = []
# N = 4 #branch 개수
# visit = [False for _ in range(N)]
#
# path = []
# def kfc(x):
#     if x == 5:
#         print(path)
#         return
#     else:
#         for i in range(1,5):
#             if visit[i-1]:
#                 continue
#             visit[i-1] = True # 1234 (1한번썼으면 뒤에는 1x ...)
#             path.append(i)
#
#             kfc(x+1)
#
#             path.pop()
#             visit[i-1] = True # 2 2부터 시작할때는 1이 들어갈수있어야함
#
# kfc(0)

#branch 는 6, lvel = N
'''
path = []
def type1(x,N):

    if x == N:
        print(path)
        return

    else:
        for i in range(1,7):
            path.append(i)
            type1(x+1,N)
            path.pop()
# 중복없는 순열
path2 = []
visit = [False for _ in range(6)]
def type2(x,N):

    if x == N:
        print(''.join(map(str, path2)), end = ' ')
        return

    else:
        for i in range(1,7):
            if visit[i-1]:
                continue
            visit[i-1] = True
            path2.append(i)

            type2(x+1,N)

            path2.pop()
            visit[i-1] = False

N, type = map(int, input().split())
type1(0, N)
type2(0, N)
'''

cnt = 0
path = []
def pb1(x,N,s):
    global cnt
    if x == N:
        if s == 10:
            cnt +=1
        return
    elif s > 10:
        return
    else:
        for i in range(1,7):
            path.append(i)
            pb1(x+1,N,s+i)
            path.pop()

pb1(0,3,0)
print(cnt)