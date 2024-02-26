
def dfs(start,goal):
    v_ed = [0] * (V+1)
    st= []
    v_ed[start] = 1 # 출발 위치 표시

    i = start # i 가 현재위치 변수
    while True: # 모든 w 방문할때까지 반복
        for w in adjl[i]:
            if v_ed[w] ==0:
                st.append(w) # 이동할거니까 이전 위치 push
                i = w # 위치 이동
                v_ed[i] = 1 # 방문체크
                break #모든 w 다 방문하면 break

        else:
            if st:
                i= st.pop() # while 문 안에 있으니까 pop 하고 다시 for문으로 이동
            else:
                if v_ed[goal] == 1:
                    return 1
                else:
                    return 0
                #break  #st가 비어있으면 브레이크


T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    adjl = [[] for _ in range(V+1)] # 인접 배열 만들어두기

    for _ in range(E):# E줄만큼 인접행렬 받을 것
        n1, n2 = map(int,input().split())
        adjl[n1].append(n2)

    start, goal = map(int, input().split()) #시작점과 끝점
    print(f'#{tc} {dfs(start,goal)}')