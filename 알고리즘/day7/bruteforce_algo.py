#고지식 알고리즘
# 본문을 처음부터 끝까지 순회
# 모든 위치에서 패턴 비교시 시간복잡도 최악은 O(MN)
p = "is"
t = "this is a book"
M = len(p)
N = len(t)


def bf(p,t):
    i = 0 #t인덱스, t길이 N
    j = 0 #p인덱스 , p길이 M

    # 패턴 내부에서만 확인할것
    while j<M and i <N:
        if t[i] != p[j]:
            i= i-j # 다를때 j 만큼 뒤로 가기
            j = -1 # 밑의 +1 을 위해 항상 -1로 초기화

        #else로 구현해도됨,else 로 만들면 j = 0으로 구현
        #else 없이 항상 동작. 무조건 1씩 더해주기
        i = i+1
        j = j+1

    if j ==M: #패턴 찾았기때문에 while 벗어남
        return i-M
    else:
        return -1


