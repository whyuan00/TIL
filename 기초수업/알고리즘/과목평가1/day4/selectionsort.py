#
# def selectionSort(arr,N):
#     for i in range(N-1):
#         min_idx = i
#         for j in range(i+1,N):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# def selectionSort(arr,N):
#     str = 0
#     while str < N:
#         min_index = str # 제일 앞의 수를 인덱스로 해줘야함
#         for j in range(str, N):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         arr[str], arr[min_index] = arr[min_index], arr[str]
#         str +=1
#     return arr

def selectionSort(a,N):
    for i in range(0,N-1): # 구간의 원소가 한개남을때까지
        min_index = i #index i, 즉 제일 앞에꺼가 젝 작다고 가정
        for j in range(i+1, N): #다음 인덱스부터 비교
            if a[min_index] >a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a




a = [1,6,8,3,3,7,4,2,2]
N = len(a)
print(selectionSort(a,N))

