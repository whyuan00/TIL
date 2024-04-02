K = 7
N = 6
data = [7,2,4,5,2,3]

counts = [0] * (K+1)
temp = [0] * N

# count 에 중복개수대로 카운트
# data의 i 요소를 i번째에 넣기
for i in data:
    counts[i] +=1

# 누적합 넣기
for i in range(1, K+1):
    counts[i] = counts[i-1] + counts[i]


#데이터 마지막 원소부터 정렬
for i in range(N-1, -1, -1):
    counts[data[i]] -= 1  # 누적합에서 개수 빼주기
    temp[counts[data[i]]] = data[i]

print(*temp)
