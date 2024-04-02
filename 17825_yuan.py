'''

모든 노드 넘버링해서 리스트에 저장
1) 전체노드 저장
2) 10/20/30만 따로 리스트에 저장  a[] b[] c[]

# 그래프 말고 p[]에 연결노드 저장하기
p = [0]*노드개수
p[x] = y  : 현재 노드x를 p에 넣으면 다음노드 y 뱉음

start = 1 final = 0
location = [0,0,0,0]
go_lst = [이동경로]
result = 0
for i in go_lst:
    for num in range(4):
        location[num] 가지고 이동

        final 아닐때
        1) x = location[num] (미리 저장하기)
        1-1) if x== a and a[i] not in location: # 갈곳에 말 있는지 확인
                location[num] =  a[i]
                result +=a[i]
            elif x == b and b[i] not in location~
            elif x==c
            elif x==d
            else:
                for _ in range(i) i횟수동안 이동하기


'''