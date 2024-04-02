N= 3
arr = [1,2,3]
#
# for i in range(1<<N): # 1<<N 부분집합의 개수
#     for j in range(N): #원소 수만큼 비트 비교
#         if i&(1<<j): # i의 j번 비트가 1인경우
#             print(arr[j], end = '') #j번 원소 출력 
#     print()

for i in range(1 << N):
    s = 0
    for j in range(N):
        if i & (1 << j):
            s += arr[j] #부분집합에 해당된 원소 합
            print(arr[j], end=' ')

    print(s)
