def f (pat, txt, len_p, len_t):

    # pat인덱스는 아무리 많이가도 txtd의 pat 길이만큼 덜간 부분에서 멈춤
    for i in range(len_t - len_p + 1):
        for j in range(len_p):
            #시작점 i 부터 pat 의 길이인 j 만큼 올때까지 모두 동일해야함
            # 그렇지 않으면 break 하고 시작점 i를 바꿈
            if txt[i+j] != pat[j]:
                break
        #모든 j에서 성공한경우(pat 를 찾은 경우)
        else:
            return 1

    # i와 j 다 돌았는데도 최종실패한 경우
    return 0


T = int(input())
for tc in range(1,T+1):
    pat = input()
    txt = input()

    len_p = len(pat)
    len_t = len(txt)

    ans = f(pat,txt,len_p, len_p)
    print(f'#{tc} {ans}')

