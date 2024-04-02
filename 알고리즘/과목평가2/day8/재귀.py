#
# #피보나치 재귀함수 -> 문제점은 중복호출. 이걸 해결하기 위해 memoization 있음
#
# def fibo(n):
#     if n<2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)


#재귀함수 접근:  i 가 현재위치, k 가 목표
def f(i,k):
    if i==k:
        pass
    else:
        print(arr[i]) # 아직 목표에 도달안했으면 현재 위치 출력
        return f(i+1,k)

arr= [10,10,30]
N = len(arr)
f(0,N)
