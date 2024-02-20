
def inorder(t):
    if t <= N:
        inorder(t*2)
        print(tree[t], end='')  # 가능하면 바로 프린트
        inorder(t*2+1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    char = [0] * (N+1)
    tree = [0] * (N+1)
    par = [0] * (N+1)
    # adjl = [[0] * (N+1)for _ in range(N+1)]

    for _ in range(N):
        x = input().split()
        idx = int(x[0])
        tree[idx] = x[1]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()
