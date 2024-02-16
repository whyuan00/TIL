# T = int(input())
# for tc in range(1,T+1):

n, lmt = map(int,input().split())
hamst = []
for _ in range(n):
    tas, cal = map(int,input().split())
    hamst.append([tas,cal])

# 비트 연산자

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(hamst[j])


#dfs?
# 재귀로 부분집합 구하기?

#1. [tas, cal] 을 다 넣은 통 리스트 만들기
#2. 통 리스트 중에 부분집합 다 탐색
#3. 탐색의 [0] 인덱스를 다 더한값 sum_tas [1] 인덱스를 다 더한값 sum_cal
# 4. if sum_tas >lmt and sum_cal > total_cal 일때 total_cal로 바꿈