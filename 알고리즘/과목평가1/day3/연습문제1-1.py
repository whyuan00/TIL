N= 5
arr = list(map(int, ...))

total = 0
for i in range(N):
        total += arr[i][i]
        total += arr[i][N-1-i]
if N%2:
    total -= arr[N//2][N//2]
print(total)

# # 자신을 기준으로 대각선들 합 구하는 함수
# # arr은 이중 배열 문
# def f(N,arr):
#
#     di = [-1,1,1,-1]
#     dj = [1,1,-1,-1]
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 if 0<= i<N and 0<= j <N :
#                     i = i + di[k] * ()
#                     j = j + dj[k] *




# N= 5
#
# data = [[]* N for _ in range(N)]
# # 순서 오른쪽 위 대각선부터 시계 방향
# di = [-1, 1, 1, -1]
# dj = [1, 1, -1, -1]

# # 현위치가 2,2 일때 첫번째 대각선들 구함
# s = 0
# for k in range(4):
#     i = 2 + di[k]
#     j = 2 + dj[k]
#     s += data[i][j]
#
# # 현위치가 2,2 일때 두번째 대각선들 구함
# k = 0
# for k in range(4):
#     i = 2 + di[k] * 2
#     j = 2 + dj[k] * 2
#     k += data[i][j]
#
# s+k 가 답?
#

# for i in range(5):
#     for j in range(5):
#         for k in range(4):
#             i = i+ di[k]
#             j = j+ dj[k]
#             print(j,k)
#         print()