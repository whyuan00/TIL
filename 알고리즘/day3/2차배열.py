di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5

for i in range(N):
    for j in range(N): #nn 행렬
            ni = i  #상하이동
            nj = j + dj[0] -1 #좌우이동

        #시작점인 0,0 에서 우 하 좌 상 지정한 순서로 1씩 이동,
        #시작점 i,j가 0,0 ~ n-1,n-1 니까 시작점에서 우 하 좌 상 1씩 이동
            print((ni,nj), end = ' ')


# N = 5
# arr = [[0] *N for _ in range(N)]
# for i in range(N):
#     for j in range(N): #nn 행렬
#         for k in range(4):
#             ni = i + di[k] #상하이동
#             nj = j + dj[k] #좌우이동
#             if 0<= ni<N and 0<nj<N:
#                 print((arr[ni],arr[nj]), end = ' ')
#         print()


# 다른 2차원 배열
#
# N = 5
# arr = [[0] *N for _ in range(N)]
# for i in range(N):
#     for j in range(N): #nn 행렬
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i+di, j+dj
#             print((ni,nj))