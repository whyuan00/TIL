


def dfs(v, end):
    visited = [0] * 100
    stack = []
    visited[v] = 1
    while True:
        if A[v] != -1 and visited[A[v]] ==0 : #현재 방문하려는 도시가 간선있고 이전방문안함
            stack.append(v)
            v = A[v]
            visited[v] = 1

        elif B[v] != -1 and visited[B[v]] ==0 :
            stack.append(v)
            v = B[v]
            visited[v] = 1

        else:
            if stack:
                v= stack.pop()
            else:
                break

        if v == end:
            return 1
    return 0



#
# for i in range(5): # 두개씩 받기
#     print(i*2,i*2+1)

T = 10
for tc in range(1,T+1):
    tc, N = map(int, input().split())
    arr = list(map(int,input().split()))

    A = [-1] * 100  # -> 0이 아닌 -1로 하면 왔다갔다 할수 있음
    B = [-1] * 100 # i와 인접한 첫번째 도시번호/두번째 도시번호

    for i in range(0,N*2,2): # 두개씩 받기
        n1, n2 = arr[i], arr[i+1]
        if A[n1] == -1:
            A[n1] = n2
        else:
            B[n1] = n2

    print(f'#{tc} {dfs(0,99)}')
