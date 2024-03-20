#서로소 집합: 특정 멤버(respresenatative) 를 통해 구분

# 연산
'''
make-set(x) / find-set(x) / union(x,y)
'''
'''
상호배타집합표현 - 연결리스트
같은 집합 원소는 하나의 연결리스트로 관리

상호배타집합표현 - 트리
자식노드가 부모노드 가리킴,
루트노드가 대표자

'''

def make_set(n):
    # 자기자신이 대표엔 데이터 6개리스트 생성
    # [0,1,2,3,4,5]
    # i 각각은 대표자 인덱스
    return [i for i in range(n)]
parent = make_set(7)
def find_set(x):
    #ㅍ대표자 찾기
    #부모 노드 보고 부모노드도 연결되어있으면 다시 반복
    # 자기자신이 대표인 데이터 찾을때까지 반복
    if parent[x]==x:
        return x
    #다음 재귀호출
    return find_set(parent[x])

#3.union
def union(x,y):
    # x의 대표와y대표 찾아서 싸이클 방지해야함
    x= find_set(x)
    y=find_set(y)
    if x==y:
        return

    if x <y:
        parent[y] = x
    else:
        parent[x] = y
print(parent)
union(1,3)
print(parent)
union(2,3)
print(parent)
union(5,6)
print(parent)

