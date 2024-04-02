#dfs 비선형 구조: 그래프 자료를 모두 빠짐없이 검색이 중요

#dfs 깊이 우선탐색: 스택을 활용할 수도 있고 다른방식으로도 가능
# 계속 탐색하다가 막히면 갈림길로되돌아와서 다시 탐색 반복해서 모든 정점 방문
# 마지막 정점에서 우선탐색 해야하니까 스택.
# 시작점 결정해


'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i):
    visited[i] = 1
    print(i)
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)

#
# def dfs(i, V): #시작 i, 마지막 V
#     visited = [0] * (V+1)
#     st = []  # visited 와 stack 은 생성 초기화해야함
#     visited[i] = 1 #시작점 방문
#     print(i) #정점에서 할일
#
#
#     while True: #탐색
#         # 현재 방문한 정점에 인접하지만 방문안한 정점w 있는지
#         for w in adjl[i]:
#             if visited[w] ==0: # 방문 안한경우
#                 st.append(i) #이전지점인 i를 스택에 추가
#                 i = w # w에 방문해서현위치를 w로 바꿔줌
#                 visited[i] = 1 #방문 표시
#                 print(i)
#                 break  # for w 를 정지
#         else: #for / else 이경우 인접점이 없으면
#             if st: #스택 비어있지 않으면 or top >-1 이면
#                 i = st.pop()
#             else: # 남은 갈림길 없으면 st비어있음
#                 break  #while true 정지
#


V,E = map(int,input().split())
arr = list(map(int,input().split()))

# 인접 리스트
adjl = [[]for _ in range(V+1)] # adfl[i] 행에 인접인 정점 번호

for i in range(E): # 숫자들을 가져오거나 / 2씩 증가하는 두개의 정점도 가능
    n1, n2 = arr[i *2], arr[i*2+1]  #두개 한쌍으로 뽑으려고 *2
    adjl[n1].append(n2)  # n1의 비어있는 리스트에 n2 추가
    adjl[n2].append(n1) # n2에도 n1이 연결되어있음 (방향이 없는 경우에 한정)
visited = [0] * (V + 1) # 빠른 번호부터 가고싶으면 adjl을 sort

dfs(2)









#bfs 너비 우선탐색