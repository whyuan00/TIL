'''

N행렬에서 매행마다 다른 열의 숫자 선택해서
최소합 구하기

p = [-.-.-.]
를 012, 021, 102 ... 등 순열로 채우기
'''

def f(i,k,s): # s는 i-1까지 선택한 합
    global cnt
    global min_v
    cnt +=1
    if i==k:
        s = 0
        for j in range(k):
            s+= arr[j][p[j]] # j행에서 p[j]열 고르기

        if min_v>s:
            min_v = s
    elif s>= min_v:
        return
    else:
        for j in range(i,k): # p[i]자리에 올 ㅇ원소p[j] 결정
            p[i] , p[j] = p[j], p[i]
            f(i+1,k, s+arr[i][p[i]])
            p[i], p[j] = p[j], p[i] # 교환 전으로 복구


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
p = [i for i in range(N)]
min_v = 100 # 넣어야할 수는 최대 100개 안넘어감
cnt = 0
f(0,N,0)
print(min_v, cnt)
# 순열 ㅏㅁㄴ들어서 for j in range(N): s+= A[j][p[j]