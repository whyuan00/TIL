T = int(input())
for tc in range(1, T+1):
    #N 은 상자 개수 Q는 작업 횟수
    N, Q = list(map(int, input().split()))
    # i번 상자 인덱스 위해 상자 N+1 개 만듦
    box = [0] * (N+1)

    for i in range(1, Q+1):
        # 바꿀 상자 구간 L 과 R
        L, R = list(map(int, input().split()))
        for j in range(L, R+1):
            box[j] = i # 구간 사이 박스를 전부 i로 바꿈

    # 앞에 있는 0 빼주기
    box.remove(0)

    print(f'#{tc}', end = ' ')
    for x in box:
        print(x, end= ' ')
    print()