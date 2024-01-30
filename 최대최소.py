T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int,input().split()))

    k = max(N_list)
    count1 = [0] * (k+1)
    count2 = [0] * (k + 1)

# 최대값 인덱스 찾기
# 인덱스 값을 count리스트 에 할당

    for i in range(N):
        count1[N_list[i]] = i

    # 뒤에서부터 0 아닌수 찾기
    for j in range(k,0, -1):
        if count1[j] != 0:
            Max_index = count1[j]
            break

# 최솟값 인덱스

    for p in N_list:
        count2[p] += 1

    for p in range(1,k+1):
        count2[p] = count2[p-1] + count2[p]

    # 누적값의 제일 앞이 작은 수
    for r in range(k+1):
        if count2[r] != 0:
            Min = r
            break

    for s in range(N):
        if N_list[s] == r:
            Min_index = s
            break

    result = Max_index - Min_index
    if result <0:
        result = - result

    print(f'#{tc} {result}')