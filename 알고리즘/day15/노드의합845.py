# 노드합은 재귀로 구현할수 있음.

#1. 재귀함수
def f(i):
    if i <= N:
        if tree[i] ==0:
            tree[i] = f(tree[i*2]) + f(tree[i*2+1])
        return tree[i]

    else:
        return 0

tree = [] # 리프노드 들어간 값
f(1) # root값 넣어주기


#2. 재귀함수

last = n
While last >0:
    tree[last//2] += tree[last]
    last -= 1



'''
T= int(input())
for tc in range(1,T+1):

    N, lfN, numN = map(int, input().split()) # 노드개수, 리프개수, 출력노드

    h = [0] *(N+1) # 힙 생성
    lf_lst = []
    for _ in range(lfN):
        lfn, key = map(int, input().split()) # lf 노드 번호, 키값
        h[lfn] = key
        lf_lst.append(lfn)

    for lf in lf_lst:
        c = lf
        while c != 0:
            p = c//2
            try: # 자식 노드 둘다 0 아닐때는 합치기
                if h[p * 2] != 0 and h[p * 2 + 1] != 0:
                    h[p] = h[p*2] + h[p*2+1]
                    c = p
                else:
                    break # 0만나면 while 에서 나와서 다음 lf 노드 찾기

            except: # 자식노드가 하나만 있으면 레인지 에러. 왼쪽 자식노드가 0이 아닐때 부모노드 값 결정
                if h[p * 2] != 0:
                    h[p] = h[p * 2]
                    c = p
                else:
                    break # 0이면 while 에서 나와서 다음 lf 노드 찾기

    print(f'#{tc} {h[numN]}')
'''