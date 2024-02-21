
N = int(input())
P= [0] * (N+1) #자식 인덱스로 부모 넣음
c = [[] for _in range (N+1)

root = 1
P[0] = root # 0에 루트 넣어주기
arr = [list(map(int,input().split())) for _ in range(N-1)]
# print(arr): [[1, 6], [6, 3], [3, 5], [4, 1], [2, 4], [4, 7]]

for i in range(len(arr)):
    if i[0] in


# while not all (arr[i] == 0 for i in range(N-1)): #리스트 안의 모든수가 0될때까지
#     for idx in range(1,N-1):
#         if arr[idx] != 0: # 0이 아닐때만 진행
#             if idx in P or c1 or c2: # idx 가 부모, arr[idx]가 자식
#                 p, c = idx, arr[idx]
#                 print(p,c)
#                 if c1[p] == 0:
#                     c1[p] = c
#                 else:
#                     c2[p] = arr[p]
#                 P[c] = p
#                 arr[idx] = 0
#
#             elif arr[idx] in P or c1 or c2: #arr[idx] 가 부모, idx 가 자식
#                 p, c = arr[idx], idx
#                 if c1[p] == 0:
#                     c1[p] = c
#                 else:
#                     c2[p] = c
#                 P[c] = p
#                 arr[idx] = 0
#         else:
#             continue #0이면 패스
# #         print(arr)
#
#
