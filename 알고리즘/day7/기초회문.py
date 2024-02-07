def f(str):
    N = len(str)
    i = 0
    j = N - 1

    # 짝수
    if N % 2 == 0:
        while 0 <= i < N // 2 and N // 2 - 1 < j <= N - 1:
            if str[i] != str[j]:
                return 0
            else:
                i += 1
                j -= 1

        # 홀수
    else:
        while 0 <= i < N // 2 and N // 2 < j <= N - 1:
            if str[i] != str[j]:
                return 0
            else:
                i += 1
                j -= 1

    return 1

T = int(input())
for tc in range(1,T+1):
    str = input()
    print(f'#{tc} {f(str)}')




