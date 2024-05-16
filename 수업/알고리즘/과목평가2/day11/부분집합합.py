'''
부분집합의 합 구할때
A= [1,2,3,4,5]
구하려는 합 = N
이때 이미 합이 N을 넘었을 경우 자르기



f(i,N,s,t), s 는 이전원소까지 고려한 합
if s ==t: 답 찾아서 출력. 단 이후에 -가 있는 경우는 다르게 풀어야함
elif i == N: 모든 원소에 대한 고려 끝난경우
elif s>t : 남은 원소 고려x일경우
else:
 subset[i] = 0
 f(i=1, N, s+A[i], t]
 subset[i] = 1
 f(i=1, N, s+A[i], t]
'''

def f(i,k,s,t):
    global cnt
    cnt +=1
    if s == t : # 답 찾은경우 해당 원소 출력
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print()

    elif i==k:
        return False

    elif s>t: #원소 합이 t보다 큰경우
        return False

    else:

        for j in range(1,-1,-1)
            bit[i] = j
            f(i+1,k,s+A[i]*j,t)
        '''
        bit[i] = 1
        f(i+1,k,s+A[i],t) # 첫번째 원소에 1넣고 s 더해주기
        bit[i] = 0
        f(i+1,k,s,t) # 0 넣고 s는 동일
        '''



A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
bit = [0] * N
cnt = 0
f(0,N,0,1)
print(f'cnt:', cnt)
'''
현재까지의 합s (s>T)말고
남은 구간의 합 rs (s+rs<t)고려할수도있음 
'''
