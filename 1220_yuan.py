# 새로운 배열에 1만 올리고 2는 그대로
def f1(arr):
    newarr = [[0] * 100 for _ in range(100)] #  매 턴마다 새로운 배열 만들기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                if 0<= i+1<N and arr[i+1][j] == 0:
                    newarr[i+1][j] = 1
                else:
                    if i+1 > N-1:
                        newarr[i][j] = 1
            elif arr[i][j] == 2:
                newarr[i][j] = 2

    return newarr
# 2만 내리고 1은 그대로
def f2(arr):
    newarr = [[0] * 100 for _ in range(100)] #  매 턴마다 새로운 배열 만들기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                 newarr[i][j] = 1

            elif arr[i][j] == 2:
                if 0<= i-1 <N and arr[i-1][j] == 0:
                    newarr[i-1][j] = 2
                else:
                    if i-1 > 0:
                        newarr[i][j] = 2
    return newarr


T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    while True:
        arrnew1 = f1(arr)
        arrnew2 = f2(arrnew1)
        if arrnew2 == arrnew1 == arr:
            break
    # for i in arr:
    #     print(i)

    # 개수 세기
    res = 0
    for i in range(100):
        cnt = 0
        now = bool(arr[i][0])  # 처음값 할당. 0 or 1
        if now == True:
            cnt +=1 # 숫자부터 시작하면 + 1 해주기
        for j in range(100):
            if bool(arr[j][i]) != bool(now):
                now = bool(arr[j][i]) # 값 바뀌면 now의 bool 값도 바꿔주기
                if now == True:
                   cnt +=1 # now 가 0이 아닌걸로 바뀔때만 +1
        res += cnt
    print(f'{tc} {res}')
