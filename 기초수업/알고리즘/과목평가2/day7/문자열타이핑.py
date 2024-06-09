T = int(input())
for tc in range(1,T+1):
    txt, pat = input().split()

    #문자열 길이
    N, M = len(txt), len(pat)

    #total은 pat 이 들어간 개수
    #cnt 는 현재 txt와 pat 가 몇개나 동일한지 카운트
    total = 0
    cnt = 0

    # i 는 txt 인덱스, j 는 pat 인덱스
    i = 0
    j = 0

    while 0<= i < N:
        print(i)
        if txt[i] == pat[j]:
            i +=1
            j +=1
            cnt +=1

            # 자리수 같을때 cnt 확인하기
            # cnt 가 pat 문자열 길이와 동일할때(즉 이미 pat가 한번들어갔을때) total+1,cnt와 j 초기화
            if cnt == M:
                total +=1
                cnt = 0
                j = 0
        else:
            i = i-(j-1) # i 돌아가기
            j = 0
            cnt = 0 # 자리수 다를때 j와 cnt 초기화

    result = N - total * M + total # N 문자열중 pat이 차지하는 부분 빼기 + pat 횟수 더하기
    print(f'#{tc} {result}')