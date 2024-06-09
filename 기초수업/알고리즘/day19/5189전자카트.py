
#000 ~ 222 중에 중복안되는순열/
#lv = 3, branch = 3


def permu(lv,sum):
    global minsum

    if lv == N-1:
        sum = sum + arr[path[-1]][path[0]]
        if sum < minsum:
            minsum = sum

    if sum > minsum:
        return

    else:
        for i in range(1,N):
            if visit[i]:
                continue
            path.append(i)
            visit[i] = True

            permu(lv+1,sum + arr[path[-2]][path[-1]])

            path.pop()
            visit[i] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minsum = 100*N*N
    path = [0]
    visit = [False for _ in range(N)]

    permu(0,0) # 자리수,sum
    print(f'#{tc} {minsum}')







# def comb(i,N):
#     global minsum
#     if i== N:
#         sum = 0
#         for j in range(N):
#             if p[j] != j: # 012 각 행에 동일 열 숫자 들어가면 안됨
#                 sum += arr[j][p[j]]
#             else:
#                 return # 같은숫자 한개라도 들어가면 중단
#         if sum < minsum:
#             minsum = sum
#     else:
#         for j in range(N):
#             p[i], p[j] = p[j], p[i]
#             comb(j+1,N)
#             p[i], p[j] = p[j], p[i]
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     p = [i for i in range(N)]
#     minsum = 0
#     for x in arr:
#         minsum += sum(x)
#
#     comb(0,N) # 0번부터 N개 순열 결정
#     print(f'#{tc} {minsum}')