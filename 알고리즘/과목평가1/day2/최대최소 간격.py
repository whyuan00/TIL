T = int(input())

for tc in (1, T+1):
    N = int(input())
    N_list = list(map(int,input().split()))

    k = max(N_list)
    count1 = [0] * (k+1)
    count2 = [0] * (k + 1)

    # 최소값 위치 Min 찾기 -> 최솟값의 이전 인덱스 찾기
    # # 인덱스 값을 count 에 할당

    for i in range(N):
        count1[N_list[i]] = i

    for j in range(1, k+1):
        count1[j] = count1[j-1] + count1[j]

    for j in range(k):
        if count1[j] != 0:
            Min = count1[j]  # Min 개 있음
            break
    print(Min)

    # # 최대값 위치 찾기
    # # 인덱스 값을 count 에 할당
    #
    # for i in range(N):
    #     count2[N_list[i]] = i
    #
    # # 뒤에서부터 0 아닌수 찾기
    # for j in (k,0, -1):
    #     if count2[j] != 0:
    #         Max = count2[j]
    #         break

    print(Max)
    result = Max - Min
    if result <0:
        result = -result

    print(f'#{tc} {result}')