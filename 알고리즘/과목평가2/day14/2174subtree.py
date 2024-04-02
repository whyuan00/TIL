
# c의 조상중에 root가 있는지 판단하는  함수
def find_root(c):
    while P[c] != 0:
        if P[c] == root:
            return True
        else:
            c = P[c]
    return False

T = int(input())
for tc in range(1,T+1):

    E, root = map(int,input().split()) # 5 1

    N = E+1
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    P = [0] * (N+1)

    lst = list(map(int,input().split())) # 2 1 2 5 1 6 5 3 6 4 # 2E
    for i in range(E): # 부모 lst[i*2], 자식 lst[i*2+1]

        if c1[lst[i*2]] == 0:
            c1[lst[i*2]] = lst[i*2+1]

        else:
            c2[lst[i * 2]] = lst[i * 2 + 1]
        P[lst[i * 2 + 1]]= lst[i * 2]


    cnt = 1
    for i in range(1,N+1):
        if find_root(i):
            cnt +=1
    print(f'#{tc} {cnt}')

