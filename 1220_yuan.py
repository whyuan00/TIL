def f(arr):
    newarr = [[0] * 100 for _ in range(100)] #  매 턴마다 새로운 배열 만들기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                if 0<= i+1<N and arr[i+1][j] == 0:
                    newarr[i+1][j] = 1
                else:
                    if i+1 != N:
                        newarr[i][j] = 1

            elif arr[i][j] == 2:
                if 0<= i-1 <N and arr[i-1][j] == 0:
                    newarr[i-1][j] = 2
                else:
                    if i-1 != -1:
                        newarr[i][j] = 2

    return newarr

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    while True:
        arrnew = f(arr)
        if arrnew == arr:
            break
        else:
            arr = arrnew
    # for i in arr:
    #     print(i)

    # 개수 세는 함수
    # res = 0
    # for i in range(100):
    #     cnt = 0
    #     now = bool(arr[i][0])  # 처음값 할당. 0 or 1
    #     for j in range(100):
    #         if bool(arr[j][i]) != bool(now):
    #             now = bool(arr[j][i]) # 값 바뀌면 now의 bool 값도 바꿔주기
    #             if now == True:
    #                cnt +=1 # now 가 0이 아닌걸로 바뀔때만 +1
    #     res += cnt
    # print(f'{tc} {res}')
