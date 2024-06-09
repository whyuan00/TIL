

T = int(input())
for tc in range(1, T+1):
    #첫번쨰 사각형의 좌표
    x1, y1, a1, b1 = map(int, input().split())

    # 두번째 사각형
    x2, y2, a2, b2 = map(int, input().split())

    fst_wide = abs(y1-b1)
    fst_length = abs(x1-a1)

    sec_wide = abs(y2-b2)
    sec_length =  abs(x2-a2)

    # 두 직사각형 합쳤을 때 비교할 기준 가로세로
    wide = fst_wide + sec_wide
    length = fst_length + sec_length

    # 최소열/ 최대열 / 최소행/ 최대행 좌표
    wide_Min = min(y1,b1,y2,b2)
    wide_Max = max(y1,b1,y2,b2)

    length_Min = min(x1,a1,x2,a2)
    length_Max = max(x1,a1,x2,a2)

    #1.  가로기준 min 과 max 차이가 가로 보다 작고
    #  세로 기준 min 과 max 차이가 세로보다 작을때 직사각형으로 겹침

    if wide_Max - wide_Min < wide and length_Max - length_Min < length:
        ans = 1

    #3. 가로기준 min 과 max 차이가 가로 같고
    #  세로 기준 min 과 max 차이가 세로 같을때  모서리 겹침
    elif wide_Max - wide_Min == wide and length_Max - length_Min == length:
        ans = 3

    #4.  가로기준 min 과 max 차이가 가로 보다 크거나
    #  세로 기준 min 과 max 차이가 세로보다 클때 (하나라도 크면) 안겹침
    elif wide_Max - wide_Min > wide or length_Max - length_Min > length:
        ans = 4

    else:  #경우의 수 많아서 그냥 else 로 처리
    # #  세로 기준 min 과 max 차이가 세로보다 작을때 선분 겹침 ( 하나 같고 하나 작을때) 등등..
    # elif wide_Max - wide_Min == wide and length_Max - length_Min < length:
    # elif wide_Max - wide_Min < wide and length_Max == length_Min < length:
        ans = 2
    print(f'#{tc} {ans}')


