'''
powerset {1,2,3,4,5,6,7,8,9,10}
중 원소합이 10인 부분집합 만드는 알고리즘


i=0일때 bit[0] 포함한 부분집합
i=1일때 bit[1] 포함 부분집합 생성
...
i=10일때 [1,2,3,4,5,6,7,8,9,10]


f(i,k) 는  bit[i] 결정 함수
if i==k:
    print나 등등
else:
    bit[i] = j
    f(i+1,k)

k = 10이 될떄까지 bit[i]자리를 결정
'''

def f(i,k,t):
    if i==k:
        ss = 0
        for j in range(k):
            if bit[j]: # bit[i] ==1 인데 bit가  전부 0아니면 1이라서 생략
                #bit에 값이 있을때 해당 인덱스의 A 값 ss에 넣어주기  /# print(A[j], end= ' ')
                ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]: # 해당 요소 포함되어 있을때만 출력
                    print(A[j], end = ' ') # a[j] 가 포함된 부분집합을 모두 출력
            print()
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j  # i에 1아니면 0 계속 넣기
        #     f(i + 1, k,t)

        bit[i] = 1 # 1넣고 다음단계 결정
        f(i+1,k,t)
        bit[i] = 0 # 0넣고 다음단계 결정
        f(i+1,k,t)




N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] *N
f(0,N,10)

