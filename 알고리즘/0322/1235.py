import sys
sys.stdin = open("input.input","r")


def findset(x):
    if p[x] == x:
        return x
    p[x] = findset(p[x])
    return p[x]

def union(x,y):
    x = findset(x)
    y= findset(y)
    if x==y:
        return
    if x>y:
        p[x] = y
        return
    elif y>x:
        p[y] = x
        return


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    graph = [[]*(N+1) for _ in range(N+1)]
    p= [i for i in range(N+1)]

    for _ in range(M):
        n1,n2 = map(int,input().split())
        if findset(n1) != findset(n2):
            union(n1,n2)

    cnt= 0
    for i in range(1,N+1):
        if i == p[i]:
            cnt +=1

    print(f'#{tc} {cnt}')