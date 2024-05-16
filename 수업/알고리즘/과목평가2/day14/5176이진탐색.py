# 완전이진탐색
# preorder 탐색 함수
# 짝수는 왼쪽, 홀수는 오른쪽에 넣기

def inorder(t):
    global num
    if t<= N:  # N까지만 넣어야함
        inorder(t*2)    # 2의 거듭제곱 수부터 왼쪽 넣기 -> tree[4] = 1, 2= 2   ...
        tree[t] = num  # 중위순서
        num +=1
        inorder(t*2+1) # 2의 거듭제곱 +1 은 오른쪽 넣기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = 1 # 넣을 숫자
    tree = [0] * (N+1)
    inorder(1) # 인덱스 1부터 트리에 넣기
    print(tree)
    # print(f'{tc} {tree[1]} {tree[N//2]}')


'''

# 완전 이진탐색
def inorder_traversal(t):
    global save
    if t:
        inorder_traversal(left[t])
        save.append(t)
        inorder_traversal(right[t])

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    a = [i for i in range(N+1)]
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    P = [[]*2 for _ in range(N+1)]

    # 트리의 인덱스 P[p]= c
    for i in range(N+1):
        while i > 1:
            if not a[i] in P[i//2]:
                P[i//2].append(a[i])
                i = i//2
            else:
                break
    # print(P)[[], [2, 3], [4, 5], [6], [], [], []]

    # left right 에 넣기
    for i in range(N+1): # 행 인덱스
        for j in range(len(P[i])):
            if P[i][j]:
                if left[i] ==0:
                    left[i] = P[i][j]
                else:
                    right[i] = P[i][j]
                par[P[i][j]] = i

    # print(left, right) # [0, 2, 4, 6, 0, 0, 0] [0, 3, 5, 0, 0, 0, 0]
    c = N
    while par[c] != 0:
        c = par[c]
    root = c
    save = [] # [4, 2, 5, 1, 6, 3]
    res = [0] * (N+1)
    inorder_traversal(root)
    # print(save)

    j = 1
    for i in save:
        res[i] = j
        j += 1
    print(f'#{tc} {res[1]} {res[N//2]}')
'''