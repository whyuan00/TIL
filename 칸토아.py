# def cantor(start, n):  # start: 시작점, n: 전체 길이
#     if n == 1:
#         return
#     ans[start + n // 3: start + (n // 3) * 2] = [' '] * (n // 3)
#     # 여기서 주어진 배열에 직접 접근한다
#     cantor(start, n // 3)  # 왼쪽
#     cantor(start + (n // 3) * 2, n // 3)  # 오른쪽
#
#
# while True:
#     # 파일 끝에 도달하면 반복문을 종료
#     try:
#         n = int(input())
#         ans = list('-' * (3 ** n))
#         cantor(0, 3 ** n)
#         print(''.join(ans))
#
#     except:
#         break

def cantor(bar):

    if len(bar) == 1:
        return bar

    bar = list(bar) # 리스트로 바꿈.
    N = len(bar) # 3
    bar[N//3:(N//3)*2] = [' '] * (N//3)
    return cantor(bar)


# 입력값 몇개 들어오는지 모르는 문제는 이렇게 처리
while True:
    try:
        N = int(input())
        bar = '-' * (3 ** N)
        cantor(bar)
        print(''.join(bar))


    except:
        break


# def cantor(a):
#     a = list(a)
#     N = len(a)
#     if N == 1:
#         return
#     else:
#         left = ''.join(map(str,a[:N//3]))
#         mid = ' ' * N//3
#         a = cantor(left)+ mid + cantor(left)
#         return a
#
# while True:
#     try:
#         p = 3
#         a = '-' * 3**p
#         cantor(a)
#         print(a)
#
#     except:
#         break


# def cantor(n):  # ans 는 배열 n: 전체 길이
#     if n == 1:
#         return '-'
#     else:
#         left = cantor(n//3)  # //으로 해야함
#         mid = ' ' * (n//3)
#         return left + mid + left
#
#
# while True:
#     # 파일 끝에 도달하면 반복문을 종료
#     try:
#         n = int(input())
#         rst = cantor(3**n)
#         print(rst)
#
#     except:
#         break
#
