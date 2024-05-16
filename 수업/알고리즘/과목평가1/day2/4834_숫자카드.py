T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count = [0] * 10

    for i in arr:
        count[i] += 1
    print(count)

    max = 0
    for j in range(10):
        if count[j] >= count[max]:
            max = j # j는 가장 많은 중복값의 인덱스, count[j] 는 가장 많은 중복 값

    max_index = count[max]

    print(f'#{tc} {max} {max_index}')



