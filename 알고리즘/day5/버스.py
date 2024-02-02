T = int(input())

for tc in range(1, T + 1):

    # 5000개 버스정류장
    # j 번째에 j 넣으려면 5001개 만들어야함
    # range 신경안쓰고 싶으면 넉넉하게 만들어주기
    arr = [0] * 5001
    # N개의 버스 노선에 +1
    N = int(input())
    for i in range(N):
        a, b = list(map(int, input().split()))
        # 만약 a,b중에 뭐가 더 큰지 안알려줬으면 그것도 확인해야함
        for j in range(a, b + 1):
            arr[j] += 1

    # P는 구해야되는 정류장 개수, c는 정류장 넘버, c_list 는 정류장 리스트
    P = int(input())

    busstop = [int(input()) for _ in range(P)]
    # c_list = []
    # for _ in range(P):
    #     c = int(input())
    #     c_list.extend([arr[c]])
    print(f'#{tc}', end = ' ')
    for i in busstop:
        print(arr[i], end = ' ')
    print()