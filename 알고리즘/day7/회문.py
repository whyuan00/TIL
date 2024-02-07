T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(8)]

    #회문 발견시 추가
    total = 0

    #가로
    for i in range(8):
        for j in range(8-(N-1)):
            s = j
            e = j+N-1
            if arr[i][s:e+1] == arr[i][s:e+1][::-1]:
                total +=1
    #세로

    for i in range(8):
        for j in range(8 - (N - 1)):
            s = j
            e = j+N-1
            while s < e:
                if arr[s][i] != arr[e][i]:  # 다 동일하고 i,j 만 반대로 써줌
                    break
                else:
                    s+=1
                    e-=1
            if s>=e:
                total+=1

    print(f'#{tc} {total}')

