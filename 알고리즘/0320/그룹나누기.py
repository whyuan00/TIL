
def union(a,b):

    while True:
        if p[a] == a:
            break
        else:
            a = p[a]

    while True:
        if p[b] == b:
            break
        else:
            b = p[b]

    p[b] = p[a] # 뒤에수의 대표자를 앞에수의 대표자로 바꿔줌
    return



T= int (input())
for tc in range(1,T+1):

    N, M = map(int, input().split())
    lst = list(map(int,input().split()))
    p = [i for i in range(N+1)]

    for i in range(0,len(lst),2):
        a, b = lst[i], lst[i+1]
        union(a,b)
    cnt = 0
    for i in range(1,N+1):
        if i == p[i]: # 대표가 여전히 자신
            cnt+=1

    print(f'#{tc} {cnt}')
