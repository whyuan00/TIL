T = int(input())

for tc in range(1, T+1):
    p, A, B = list(map(int, input().split()))
    la = 1
    ra = p
    lb = 1
    rb = p

    # A 찾기
    A_count = 0
    while True:
        mid = int((la+ra)/2)
        A_count += 1
        if A == mid:
            break
        else:
            if A > mid:
                la = mid
            else:
                ra = mid

    # B
    B_count = 0
    while True:
        mid = int((lb + rb)/2)
        B_count += 1

        if B == mid:
            break
        else:
            if B > mid:
                lb = mid
            else:
                rb = mid

    if A_count > B_count:
        result = 'B'
    elif A_count < B_count:
        result = 'A'
    else:
        result = '0'

    print(f'#{tc} {result}')