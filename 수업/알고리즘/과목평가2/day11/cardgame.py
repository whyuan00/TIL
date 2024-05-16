def win(x,y):
    a= A[x]
    b= A[y]
    if a == b:
        return x
    elif {a,b} == {1,3}:
        if a==1:
            return x
        else:
            return y
    elif {a,b} == {2,3}:
            if a==3:
                return x
            else:
                return y
    elif {a,b} == {1,2}:
            if a==2:
                return x
            else:
                return y

def f(i,j):
    if i==j:
        return i
    else:
        left = f(i,(i+j)//2)
        right = f((i+j)//2+1,j)
        return win(left,right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = [0]+ list(map(int,input().split()))
    print(f'#{tc} {f(1,N)}')





# def win(a, b):
#     # 가위1 바위2 보3 2>1, 3>2, 1>3
#     if card[b] - card[a] == 1 or card[b] - card[a] == -2:  # 승자b
#         return b
#     else:
#         return a
#
#
# def f(i, j):  # i~j번 사이 승자를 리턴하는 함수
#     if i == j:  # 한명인 경우 부전승
#         return i
#     else:
#         x = f(i, (i + j) // 2)
#         y = f((i + j) // 2 + 1, j)
#         return win(x, y)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())  # 학생수, 1~N번까지
#     card = [0] + list(map(int, input().split()))
#     print(f'#{tc} {f(1, N)}')






# def f1(n,i,j,k):
#     global A1
#
#     if n==k:
#         return
#
#     else:
#         st1.append(A1[:(i+j)//2+1])
#
#         s = (i+j)//2
#         A1 = A1[:(i + j) // 2 + 1]
#         f1(n+1,i,j,k)
#
#
# def f2(n,i,j,k):
#     global A2
#
#     if n==k:
#         return
#
#     else:
#         st2.append(A2[(i + j) // 2 + 1:])
#         i = (i+j)//2+1
#         A2 = A2[(i + j) // 2 + 1:]
#         f2(n+1,i,j,k)
#
# st1 = []
# st2 = []
# A1 = [2, 1, 1, 2, 3, 3 ]
# A2 = [2, 1, 1, 2, 3, 3 ]
# i = 0
# N = len(A1)
# N = len(A2)
#
#
# f1(0,0,N-1,N//2)
# f2(0,0,N-1,N//2)
# print(st1)
# print(st2)






