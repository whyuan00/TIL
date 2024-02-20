'''
순회는 모든 곳을 중복없이 방문하기
트리는 비선형구조.
선형구조와 같이 선후 연결 알기가 어려움
'''

# 1. 전위순회 : 부모노드 방문후 자식노드 좌우 순서
# 2. 중위순회 : 왼쪽자식-부모-오른쪽 자식 순서
# 2. 후위순회 : 왼쪽자식 오른쪽 자식 부모 순서



# 배열
'''
완전 이진트리에서 각 노드에 1부터 n까지 번호 부여,
[] * n에 노드 이름 저장

현재 노드의 인덱스 i 기준
i//2 들은 i의 조상 
왼쪽 자식은 i*2, 오른쪽은 i*2+1 

# 배열에 저장할경우
부모p = [0,1,2,3,4,5] n까지의 인덱스, c1과 c2에 차례로 자식 채우기 
자식c1 = [] c1[0] = 자식노드 
자식c2 = []   if c1[0] != 0, c2[0] = 자식노드 


# 루트 찾기
계속 부모 찾다가 부모없으면 해당 정점이 루트 
c = 5:
while p[c] != 0
    c= p[c] 새로운 부모 확인 
root = c 

'''
# 순회
def pre_order(T):
    if T:
        print(T,end = ' ')
        pre_order(left[T])
        pre_order(right[T])


N = int(input())
E = N-1 #간선은 정점 개수보다 한개 적음
arr = list(map(int,input().split()))
left = [0] * (N+1) # 부모 인덱스로 왼쪽 자식 번호 저장
right = [0] * (N+1) # d오른쪽 자식
par = [0] * (N+1) # 자식 인덱스로 부모 저장

# 트리 정보 저장
for i in range(E): # 간선 개수
    p, c = arr[i*2], arr[i*2+1]
    if left[p] ==0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

# 부모 찾기
c = N
while par[c]!=0:
    c = par[c]
root = c
print(root)