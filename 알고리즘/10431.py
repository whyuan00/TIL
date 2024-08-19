T = int(input())
for tc in range(1,T+1):
    res =0
    students = list(map(int,input().split()))[1:]
    line = []
    while students:
        now_st = students.pop(0)
        line.append(now_st) # 일단 맨 뒤에 넣기
        now_idx = line.index(now_st)
        # 현재 넣은 수의 앞에 있는 수와 비교
        # 앞 수가 크면 자리 바꿔주기
        while now_idx-1>=0 and line[now_idx-1] > now_st:
            line[now_idx] = line[now_idx-1]
            line[now_idx-1] = now_st
            res +=1
            now_idx = line.index(now_st)
    print(tc,' ',res)