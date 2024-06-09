T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input()) + ['0'] # ['1', '0' ] 끝이 0인 문자열 리스트로 받기
    N += 1 # 0더했으니까 N에 0 더해줌

    max_c = 0
    cnt = 0
    for i in arr:
        if i == '0':
            if cnt > max_c:
                max_c = cnt
                cnt = 0
        else:
            cnt += 1

    print(f'#{tc} {max_c}')
