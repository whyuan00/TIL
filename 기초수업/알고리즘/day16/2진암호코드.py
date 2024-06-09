dic = {'0001101': 0,
       '0011001':1,
       '0010011':2,
       '0111101':3,
       '0100011':4,
       '0110001':5,
       '0101111':6,
       '0111011':7,
       '0110111':8,
       '0001011':9
}

def f():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                ni, nj = i, j
                return (ni,nj)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]# 변환하려면 리스트로
    res = ''

    # 탐색
    ni, nj = f()

        # 맞는식
    for p in range(nj+1,-1,-7):
        strs = ''.join(map(str,arr[ni][p-7:p]))
        if strs in dic:
            res += str(dic[strs])

    # print(res)

    '''
    # 틀린식
    while 문에서 빠져나올때는 종료조건 확실하게 지정해줘야함
    
    x = 0
    y  = nj - x + 1

    while y-7>= 0:
        strs = ''.join(map(str,arr[ni][y-7:y]))
        if strs in dic:
            res += str(dic[strs])
            x+=7
        else:
            break 
    '''

    sum = 0
    ans = 0
    # print(res)
    for i in range(len(res)//2):
        sum += int(res[i*2])
        sum += int(res[i * 2 + 1]) * 3

        ans += int(res[i * 2])
        ans += int(res[i * 2 + 1])

    if sum % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {0}')
