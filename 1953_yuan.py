dic = {1: [(-1,0),(1,0),(0,1),(0,-1)],
       2: [(-1,0),(1,0)],
       3: [(0,-1),(0,1)],
       4: [(-1,0),(0,1)],
       5: [(1,0),(0,1)],
       6: [(1,0),(0,-1)],
       7: [(-1,0),(0,-1)]
       }

# print(dic['1'])
# print(dic['1'][0])
# print(dic['1'][0][0])



# bfs 는 visit 수 세야함
# #dfs
#
# # 탈주범 위치 지정 함수
# def dfs(a,t): # 현위치a, 최종횟수 0dx
#     i, j = a
#     if t == time:
#         if a not in now_lst:
#             now_lst.append(a)
#         return
#     else:
#         for x in range(1,7+1):
#             if 0<=i<N and 0<=j<M and arr[i][j] == x:
#                 for k in range(len(dic[x])):
#                     a = (i+ dic[x][k][0], j + dic[x][k][1])
#                     dfs(a,t+1)
#
# T = int(input())
# for tc in range(1,T+1):
#     N, M, x, y, time = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     now_lst = []
#     a = (x,y)
#     dfs(a,0)
#
#     print(f'#{tc} {len(now_lst)+1}')