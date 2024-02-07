# 불일치 발생 스트링문자에 대해 다시 비교안하고 매칭.
# 동일 문자열만큼 점프해서 재매칭해서 비교횟수 훨씬 적음
# 단 문자열 형태에 따라 가능여부 다름
# 시간복잡도 O(M+N) / 세타(n) 항상이정도 걸림

def kmp(t,p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

    j = 0 # 일치 개수 == 비교 패턴 위치
    lps[0] = -1 # 일단 넣어주기
    for i in range(1,M):
        lps[i] = j  # lps 에 일단 0 넣기


        # j 는 0부터 시작하는 포인터, i는 1부터 시작하는 포인터
        #p가 동일 문자 없으면 i와 j의 범위가 계속 벌어짐
        #그러다 동일 문자 발견하면 j=1
        #그 다음에도 동일하면 j+=1  ... p가 동일 패턴으로 이뤄진 경우 해당 패턴을 나타내는 lps 갖게됨
        if p[i] == p[j]:
            j +=1 # 패턴 같은 개수만큼 j 에 +1
        else:
            j = 0
    lps[M] = j #i 범위가 M-1까지라 마지막은 비어있음. 마지막 lps 칸에 j 넣어줌.

    #여기서부터 검색
    i = 0
    j = 0
    while i<N and j < M:
        if j==-1 or t[i] == p[j]:  #t와 p 비교 시작 /
            i +=1                 #이전 번에 패턴 달라서 j 초기화 된경우 +1 해주기, i+1 해서 t의 비교 시작점 변경
            j +=1                  # 같은 문자 찾았을 때 j는 초기화 안되고 +1
        else:
            j = lps[j]  # 패턴 다를떄 j의 초기화값은 -1이 아닌 lps 해당 칸에 저장된 반복값, 즉 인덱스 3으로 돌아감.
        if j==M: #  문자열 개수와 j가 동일한 경우 패턴찾은 것
            print(i-M, end = ' ') #txt 에서 패턴 찾았을때의 끝자리 인덱스 - 패턴길이 = 패턴 시작점 인덱스 출력


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t,p)