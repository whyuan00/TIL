# 새노드 추가
# 자식 > 부모
# 7,2,5,3,4,6

T= int(input())
for tc in range(1,T+1):
    N = int(input()) # 노드수
    arrn = list(input().split())
    h = [0] * (N+1) # 최대힙 , 노드 번호에 따른 값 저장할 것
    last = 0 #마지막 노드번호

    for n in arrn:
        last +=1 # 노드 생성
        h[last] = int(n) # 노드에 키값 저장

        c = last # 자식 노드
        p = last//2  # 부모 노드
        while p >=1 and h[p] > h[c]: # 최소 힙만드는 문제임
            h[p], h[c] = h[c], h[p]
            c = p # 현재노드를 부모노드로 해서 다시 진행
            p = c//2

    # print(h) :저장된 최소 힙

    # h[last]의 조상노드 찾기
    anc = 0
    c = last
    while h[c] != 0:
        p = c//2 # 부모노드 찾기
        anc += h[p] # 부모값 더해주기
        c = p # 부모노드값을 다시 자식노드에 할당

    print(f'#{tc} {anc}')




