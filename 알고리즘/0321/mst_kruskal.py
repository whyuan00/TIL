'''
임의정점 하나 선택해서 최소비용간선만 선택 -> 우선순위 큐로 구현현
1. 전체 그래프 보고 가중치가 제일작은 간선부터 뽑기
-> 코드 구현시 전체 간선정보 저장, 가중치정렬(힙큐)
2. 방문 처리 (싸이클 발생 방지)
싸이클 여부: union-find 로 확인

'''

def find_set(x):
    if p[x] ==x :
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x==y:
        return
    if x<y:
        p[y] = x
        return
    if x>y:
        p[x] = y
        return

V, E = map(int, input().split())
# 인접리스트트로저장( 실습시간에는 인접리스트저장)

edges = []

for _ in range(E):
    s,e,w = map(int,input().split())
    # 가중치 그래프 3-> 4 로 가는데 31 비용듦

    edges.append([s,e,w])

edges.sort(key=lambda x: x[2])

cnt = 0 #간선개수가 v-1이면 끝남
p = [i for i in range(V)]
sum_weight = 0

for s, e, w in edges: # 간선모두확인
    #싸이클 발생하면 pass, 없으면 통과
    # 이미 같은집합에 있어도 pass
    if find_set(s)==find_set(e):
        print(s,e,w,'싸이클발생')
        continue
    union(s,e) # 사이클 없으면 유니온
    sum_weight +=w
    cnt+=1 # 연결할때 +1

    #한개 연결하면 cnt+1
    if cnt ==V-1: #mst 완성, 간선개수 -1
        break

print(f'최소비용 = {sum_weight}')