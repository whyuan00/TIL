
def f(N):
    res = ''
    power = -1
    #N이 0될때까지 계속 빼기. 또는 길이 13되면 멈추기
    while N != 0 and len(res) < 13:
        if N - (2 ** power) >= 0:
            N -= (2 ** power)
            res += '1'
        else:
            res += '0'
            pass
        power -= 1

    if len(res) == 13:
        return 'overflow'
    else:
        return res



T = int(input())
for tc in range(1,T+1):
    N = float(input())
    print(f'#{tc} {f(N)}')