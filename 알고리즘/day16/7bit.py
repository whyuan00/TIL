# 16비트 연산법
'''
a = 149
print(f'{a:04X}')
'''

def f(a):
    '''
    7bit  10진수 변환 함수
    '''
    # a = lst = [0, 0, 0, 0, 0, 0, 0] 형식
    sum = 0
    power = 6
    for i in a:
        sum += i * (2 ** power)
        power -= 1

    return sum


T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,list(input())))

    print(f'#{tc}', end=' ')
    for n in range(0,70,7):
        x = arr[n:n+7] # 7개씩 잘라서 변환
        print(f(x), end = ' ')
    print()