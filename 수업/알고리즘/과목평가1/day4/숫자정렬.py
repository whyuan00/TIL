T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            if arr[j] <= arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f'#{tc}', end = '')
    for x in arr:
        print(x, end = ' ')
    print()


