def cantor(bar):
    if len(bar) == 1:
        return bar

    N = len(bar)
    divided_length = N // 3
    cantor_bar = list(bar)

    # Cantor set 생성
    for i in range(1, 3):
        start = divided_length * i
        end = divided_length * (i + 1)
        cantor_bar[start:end] = [' '] * divided_length

    return ''.join(cantor_bar)


# 입력값 처리
while True:
    try:
        N = int(input())
        if N < 0:
            break
        bar = '-' * (3 ** N)
        print(cantor(bar))
    except ValueError:
        print("올바른 숫자를 입력하세요.")
