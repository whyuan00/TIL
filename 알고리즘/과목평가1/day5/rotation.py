
# arr 받아서 90도 돌리는 함수 만들기
def rot(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N-1-i] = arr[i][j]

    return new_arr

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도씩 돌리기
    rot90 = rot(arr,N)
    rot180 = rot(rot90,N)
    rot270 = rot(rot180,N)

    print(f'#{tc}')
    for x in range(N):
        print(''.join(map(str,rot90[x])), ''.join(map(str,rot180[x])), ''.join(map(str,rot270[x])))