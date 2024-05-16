for _ in range(1,11):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 현위치 i, j = 99, a
    i = 99
    for a in range(100):
        if arr[i][a] == 2:
            j = a #57

    while i > 0:
        if 0<=j+1<100 and arr[i][j+1] == 1:
                while 0<=j+1<100 and arr[i][j+1] == 1:
                    j= j+1
                i = i-1

        elif 0<=j-1<100 and arr[i][j-1] == 1:
                while 0<=j-1<100 and arr[i][j -1] == 1:
                    j = j-1
                i = i-1
        else:
            i = i-1

    print(f'#{tc} {j}')

