
T = int(input())
for tc in range(1, T+1):

    N = 6
    N_list = input()
    c = [0] * 10 # 숫자 0~9 총 10개

    tri = 0
    r = 0

    for i in range(N):
        c[int(N_list[i])] += 1


    for i in range(10):
        if c[i] >= 3:
            while c[i] >= 3:
                tri += 1
                c[i] -= 3


    for j in range(8):
        if c[j]>=1 and c[j+1]>=1 and c[j+2]>=1:# 범위 설정할때 각각에 값 제한 두기
            while c[j]>=1 and c[j+1]>=1 and c[j+2]>=1:
                c[j] -= 1
                c[j+1] -= 1
                c[j+2] -= 1
                r += 1

    if tri + r == 2:
        result = 'Baby Gin'
    else:
        result = 'Lose'

    print(f'#{tc} {result}')