# 풀이1. 파리와 시간
#   곱셈먼저하기
'''

T = int(input())
for tc in range(1,T+1):
    D, A, B, F = map(int, input().split())

    #파리가 움직인 시간 = 기차ab가 충돌하기 전까지 걸린시간

    # D = AT+ BT
    # T =  D / (A + B)

    # 나눗셈은 오차가 커지기때문에 곱셈부터 먼저 시행
    result = D * F / (A+B)
    print(f"{tc} {result}")
'''
# 원안의점
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            # x**2 + y**2 <= N:
            # cnt =1

            if x**2 + y**2 <= N **2:
                cnt =1
    print(f'#{tc} {cnt}')
'''
#퍼펙트 셔플: 투포인트
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = input().split()

    i = 0
    j = (N+1)//2
    print(f'#{tc}', end = ' ')
    for turn in range(N):
        if turn % 2 == 0: # 짝수일때
            print(lst[i], end = ' ')
            i += 1
        else:
            print(lst[j], end = ' ')
            j +=1
    print()
'''
# 전봇대
'''

'''

def get_result():
    N = len(arr)
    cnt = 0
    for i in range(N):
        for tar in range(i):

            ia, ib = (arr[i][0], arr[i][1])
            ta, tb = (arr[tar][0], arr[tar][1])
            if ib < tb:
                cnt +=1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for n in range(N):
        a, b = map(int, input().split())
        arr.append((a,b))

    arr.sort(key = lambda x: x[0])
    result = get_result()
    print(f'#{tc} {result}')

#swea 20439